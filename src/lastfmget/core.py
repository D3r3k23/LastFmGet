from .errors import *
import requests
import yaml
import time
import os.path
from collections import namedtuple

Config = namedtuple('Config', [
    'api_url',
    'api_key',
    'headers',
    'call_interval',
    'cache_enabled'
])

CFG = None

ready = False
lastrequesttime = None

def init(cfg_fn):
    """
    Set up LastFmApi using api_cfg.yaml file.

    * Should only be called once at start of program

    Arguments:
      * cfg_fn (str) -- path to api_cfg YAML file
    """
    global CFG
    global ready

    with open(cfg_fn, 'r') as f:
        api_cfg_yaml = yaml.safe_load(f)
    
    headers = { 'user_agent': api_cfg_yaml['user_agent'] }

    callinterval = 1 / api_cfg_yaml['call_rate']

    cache = api_cfg_yaml['cache']

    CFG = Config(
        api_url       = api_cfg_yaml['api_url'],
        api_key       = api_cfg_yaml['api_key'],
        headers       = headers,
        call_interval = callinterval,
        cache_enabled = cache['enable']
    )

    if CFG.cache_enabled:
        dir      = cache.get('dir',      default='.cache'),
        backend  = cache.get('backend',  default='sqlite'),
        lifetime = cache.get('lifetime', default=60)

        __setup_cache(dir, backend, lifetime)

    ready = True

def __setup_cache(dir, backend, lifetime):
    """
    Imports requests_cache and installs with configuration.

    Arguments:
      * dir (str) -- Cache location
      * backend (str) -- cache backend
      * lifetime (int) -- expire_after time in seconds
    """
    import requests_cache
    requests_cache.install_cache(
        cache_name=os.path.join(dir, 'lastfmget_cache'),
        backend=backend,
        expire_after=lifetime
    )

def __get_response(payload):
    """
    Gets a response from requests.

    * Appends API key and format to the payload
    * Formats response with JSON
    * Called by raw_methods
    * Raises exceptions for known Last.fm errors and requests exceptions otherwise
    
    Arguments:
      * payload (dict) -- Data for specific request
        * method (str) -- Last.fm API method name
        * params -- Last.fm API method params

    Returns:
      Dict with response data
    """
    global lastrequesttime

    if not ready:
        raise NotConfiguredError

    payload['api_key'] = CFG.api_key
    payload['format']  = 'json'

    __rate_limiter()
    response = requests.get(CFG.api_url, headers=CFG.headers, params=payload)
    responsejson = response.json()

    if not CFG.cache_enabled or not response.from_cache:
        lastrequesttime = time.time() # Update time of last API call
    
    if 'error' in responsejson:
        if responsejson['error'] == LastFmErrorCodes.InvalidParams.value:
            raise ParamError(responsejson['message'])
        elif responsejson['error'] == LastFmErrorCodes.InvalidApiKey.value:
            raise ApiKeyError
        elif responsejson['error'] == LastFmErrorCodes.Offline.value:
            raise OfflineError
        elif responsejson['error'] == LastFmErrorCodes.RateLimit.value:
            raise RateLimitError
        else:
            raise LastFmError(responsejson['message'])
    elif not response.ok:
        response.raise_for_status()
    else:
        return responsejson

def __rate_limiter():
    """
    Waits until the required interval between API requests is reached.
    """
    if lastrequesttime is not None: # If there was a previous call to the API
        timesince = time.time() - lastrequesttime
        if timesince < CFG.call_interval:
            time.sleep(CFG.call_interval - timesince)
