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

    Globals:
      * CFG
      * ready

    Arguments:
      * cfg_fn (str) -- path to api_cfg YAML file
    """
    global CFG
    global ready

    api_cfg_yaml = __load_yaml(cfg_fn)
    
    headers = { 'user_agent': api_cfg_yaml['user_agent'] }
    callinterval = 1 / api_cfg_yaml['call_rate']
    cacheoptions = api_cfg_yaml['cache']

    CFG = Config(
        api_url       = api_cfg_yaml['api_url'],
        api_key       = api_cfg_yaml['api_key'],
        headers       = headers,
        call_interval = callinterval,
        cache_enabled = cacheoptions['enable']
    )

    if CFG.cache_enabled:
        dirname  = cacheoptions.get('dir',      default='.cache'),
        backend  = cacheoptions.get('backend',  default='sqlite'),
        lifetime = cacheoptions.get('lifetime', default=60)

        __setup_cache(dirname, backend, lifetime)

    ready = True

def __load_yaml(yaml_fn):
    """
    Loads the contents of a YAML file.

    Arguments:
      * yaml_fn (str) -- YAML filename
    """
    with open(yaml_fn, 'r') as f:
        return yaml.safe_load(f)

def __setup_cache(dirname, backend, lifetime):
    """
    Imports requests_cache and installs with configuration.

    * Private function

    Arguments:
      * dirname (str) -- Cache location
      * backend (str) -- cache backend
      * lifetime (int) -- expire_after time in seconds
    """
    import requests_cache
    requests_cache.install_cache(
        cache_name   = os.path.join(dirname, 'lastfmget_cache'),
        backend      = backend,
        expire_after = lifetime
    )

def __get_response(payload):
    """
    Gets a response from requests.

    * Private function
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
    if not ready:
        raise NotConfiguredError

    payload['api_key'] = CFG.api_key
    payload['format']  = 'json'

    __rate_limiter()
    response = requests.get(CFG.api_url, headers=CFG.headers, params=payload)
    responsejson = response.json()

    if not CFG.cache_enabled or not response.from_cache:
        __update_last_request_time()
    
    # Check for Last.fm errors
    if 'error' in responsejson:
        raise_lastfm_error(responsejson['error'], responsejson['message'])
    
    # Check for requests errors
    elif not response.ok:
        response.raise_for_status()
    
    # Response OK
    else:
        return responsejson

def __update_last_request_time():
    """
    Sets lastrequesttime to the current time.

    Globals:
      * lastrequesttime
    """
    global lastrequesttime

    lastrequesttime = time.time()

def __rate_limiter():
    """
    Waits until the required interval between API requests is reached.

    * Private function
    """
    if lastrequesttime is not None: # If there was a previous call to the API
        timesince = time.time() - lastrequesttime
        if timesince < CFG.call_interval:
            time.sleep(CFG.call_interval - timesince)
