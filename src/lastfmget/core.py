"""
Core functions for lastfmget.

Example api_cfg.yaml file:
```
api_url: http://ws.audioscrobbler.com/2.0/
api_key: <API KEY>
user_agent: <USER AGENT>
call_rate: 5 # Calls per second
cache:
  enable: true
```
"""
from .errors import *

import requests
import yaml

import time
from collections import namedtuple

Config = namedtuple('Config', [
    'api_url',
    'api_key',
    'headers',
    'call_interval',
    'cache_enabled'
])

RESPONSE_FORMAT = 'json'

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
    if not api_cfg_yaml:
        raise LastFmGetError(f'api_cfg YAML: ({cfg_fn}) not found')

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
        __setup_cache(cacheoptions)

    ready = True

def __get_response(payload, firstattempt=True):
    """
    Gets a response from requests.

    * Private function
    * Appends API key and format to the payload
    * Formats response with JSON
    * Called by raw_methods
    * Raises exceptions for known Last.fm errors and requests exceptions otherwise
    * If LastFmGet error detected then one mroe attempt will be made

    Arguments:
      * payload:
      ```
      {
        'method' (str) -- Last.fm API method name
        params -- Last.fm API method params
      }
      * firstattempt (bool) -- If this call if the first attempt to get a response
      ```

    Returns:
      Dict with response data
    """
    if not ready:
        raise NotConfiguredError

    payload['api_key'] = CFG.api_key
    payload['format']  = RESPONSE_FORMAT

    __rate_limiter()
    try:
        response = requests.get(CFG.api_url, headers=CFG.headers, params=payload)
    except requests.exceptions.ConnectionError:
        raise LastFmGetError('No internet connection found')
    responsejson = response.json()

    if not __response_from_cache(response):
        __update_last_request_time()

    # Check for Last.fm errors
    if 'error' in responsejson:
        try:
            raise_lastfm_error(responsejson['error'], responsejson['message'])
        except LastFmError:
            if firstattempt:
                # Try again one time for a response error. Necessary due to occasional random errors
                # e.g. "Operation failed: Most likely the backend service failed. Please try again."
                return __get_response(payload, firstattempt=False)
            else:
                raise

    # Check for requests errors
    elif not response.ok:
        response.raise_for_status()

    # Response OK
    else:
        return responsejson

def __load_yaml(yaml_fn):
    """
    Loads the contents of a YAML file.

    Arguments:
      * yaml_fn (str) -- YAML filename

    Returns:
        Loaded YAML file, None if not found
    """
    try:
        with open(yaml_fn, 'r') as f:
            return yaml.safe_load(f)
    except (OSError, IOError):
        return None

def __setup_cache(options):
    """
    Imports requests_cache and installs with configuration.

    * Private function

    Arguments:
      * dirname (str) -- Cache location
      * backend (str) -- Cache backend
      * lifetime (int) -- expire_after time in seconds
    """
    import requests_cache

    dirname  = options.get('dir',     '.cache')
    backend  = options.get('backend', 'sqlite')
    lifetime = options.get('lifetime', 60)

    requests_cache.install_cache(
        cache_name   = f'{dirname}/lastfmget_cache',
        backend      = backend,
        expire_after = lifetime
    )

def __response_from_cache(response):
    """
    Returns true if the reponse was from the cache
    """
    return CFG.cache_enabled and response.from_cache

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
