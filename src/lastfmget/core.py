from .exceptions import *
import requests
import yaml
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
    Set up LastFmApi using api_cfg.yaml file
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
        requests_cache.install_cache()

    ready = True

def __get_response(payload):
    """
    Appends API key and format to the payload and returns the formatted API Response
    """
    global lastrequesttime

    if not ready:
        raise NotConfiguredError

    payload['api_key'] = cfg.API_KEY
    payload['format']  = 'json'

    __rate_limiter()
    r = requests.get(cfg.API_URL, headers=cfg.HEADERS, params=payload)
    response = r.json()

    if cfg.USE_CACHE and 'from_cache' not in response:
        lastrequesttime = time.time() # Update time of last API call
    
    if 'error' in response:
        if response['error'] == LastFmErrorCodes.InvalidApiKey.value:
            raise ApiKeyError
        elif response['error'] == LastFmErrorCodes.Offline.value:
            raise OfflineError
        elif response['error'] == LastFmErrorCodes.RateLimit.value:
            raise RateLimitError
        else:
            raise LastFmError(response['message'])
    else:
        return response

def __rate_limiter():
    """
    Waits until the required interval between API requests is reached
    """
    if lastrequesttime is not None: # If there was a previous call to the API
        timesince = time.time() - lastrequesttime
        if timesince < cfg.CALL_INTERVAL:
            time.sleep(cfg.CALL_INTERVAL - timesince)
