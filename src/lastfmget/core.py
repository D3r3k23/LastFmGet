from .errors import *
import requests
import yaml
import os.path
import time
from collections import namedtuple

Config = namedtuple('Config', [
    'API_URL',
    'API_KEY',
    'HEADERS',
    'USE_CACHE',
    'CALL_INTERVAL'
])

cfg = None

ready = False
lastrequesttime = None

def init(cfg_fn):
    """
    Set up LastFmApi using api_cfg.yaml file.

    * Should only be called once at start of program.

    Arguments:
      * cfg_fn (str) -- path to api_cfg YAML file
    """
    global cfg
    global ready

    with open(cfg_fn, 'r') as f:
        api_cfg_yaml = yaml.safe_load(f)
    
    headers = { 'user_agent': api_cfg_yaml['user_agent'] }

    callinterval = 1 / api_cfg_yaml['call_rate']

    cfg = Config(
        API_URL       = api_cfg_yaml['api_url'],
        API_KEY       = api_cfg_yaml['api_key'],
        HEADERS       = headers,
        USE_CACHE     = api_cfg_yaml['use_cache'],
        CALL_INTERVAL = callinterval
    )

    if cfg.USE_CACHE:
        import requests_cache
        requests_cache.install_cache(
            cache_name=os.path.join('.cache', 'lastfmget_cache'),
            backend='sqlite',
            expire_after=120
        )

    ready = True

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

    payload['api_key'] = cfg.API_KEY
    payload['format']  = 'json'

    __rate_limiter()
    response = requests.get(cfg.API_URL, headers=cfg.HEADERS, params=payload)
    responsejson = response.json()

    if not cfg.USE_CACHE or not response.from_cache:
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
        if timesince < cfg.CALL_INTERVAL:
            time.sleep(cfg.CALL_INTERVAL - timesince)
