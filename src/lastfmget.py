import requests
import yaml
import time
import sys

#=============================================-#
#----------------| API config |----------------#
#==============================================#

API_URL       = ''
API_KEY       = ''
HEADERS       = {}
USE_CACHE     = False
CALL_INTERVAL = 1

ready = False
lastrequesttime = None

def init(cfg_fn):
    """
    Set up LastFmApi using api_cfg.yaml file
    """
    global API_URL
    global API_KEY
    global HEADERS
    global USE_CACHE
    global CALL_INTERVAL
    global ready

    with open(cfg_fn, 'r') as f:
        cfg = yaml.load(f)
    
    API_URL    = cfg['api_url']
    API_KEY    = cfg['api_key']
    user_agent = cfg['user_agent']
    USE_CACHE  = cfg['use_cache']
    call_rate  = cfg['call_rate']

    HEADERS = { 'user_agent': user_agent }

    if USE_CACHE:
        try:
            import requests_cache
        except ImportError:
            sys.exit('use_cache is selected and requests_cache could not be imported.')
        
        requests_cache.install_cache()

    CALL_INTERVAL = 1 / call_rate

    ready = True

#======================================================-#
#----------------| API method wrappers |----------------#
#=======================================================#

def user_info(self, user):
    """
    user.getInfo
    """
    payload = {
        'method' : 'user.getInfo',
        'user'   : user
    }
    return __get_response(payload)

def user_recent_tracks(self, user, limit=50, page=1):
    """
    user.getRecentTracks
    """
    payload = {
        'method' : 'user.getRecentTracks',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_top_artists(self, user, limit=50, page=1):
    """
    user.getTopArtists
    """
    payload = {
        'method' : 'user.getTopArtists',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_top_albums(self, user, limit=50, page=1):
    """
    user.getTopAlbums
    """
    payload = {
        'method' : 'user.getTopAlbums',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_top_tracks(self, user, limit=50, page=1):
    """
    user.getTopTrack
    """
    payload = {
        'method' : 'user.getTopTracks',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_weekly_chart_list(self, user):
    """
    user.getWeeklyChartList
    """
    payload = {
        'method' : 'user.getWeeklyChartList',
        'user'   : user
    }
    return __get_response(payload)

def user_weekly_artists_chart(self, user, start=0, end=0):
    """
    user.getWeeklyArtistChart
    """
    payload = {
        'method' : 'user.getWeeklyArtistChart',
        'user'   : user,
        'from'   : start,
        'to'     : end
    }
    return __get_response(payload)

def user_weekly_albums_chart(self, user, start=0, end=0):
    """
    user.getWeeklyAlbumChart
    """
    payload = {
        'method' : 'user.getWeeklyAlbumChart',
        'user'   : user,
        'from'   : start,
        'to'     : end
    }
    return __get_response(payload)

def user_weekly_tracks_chart(self, user, start=0, end=0):
    """
    user.getWeeklyTrackChart
    """
    payload = {
        'method' : 'user.getWeeklyTrackChart',
        'user'   : user,
        'from'   : start,
        'to'     : end
    }
    return __get_response(payload)

#=====================================================#
#----------------| Private functions |----------------#
#=====================================================#

def __get_response(self, payload):
    """
    Appends API key and format to the payload and returns the formatted API Response
    """
    global lastrequesttime

    payload['api_key'] = API_KEY
    payload['format']  = 'json'

    __rate_limiter()
    response = requests.get(API_URL, headers=HEADERS, params=payload)

    if USE_CACHE and 'from_cache' not in response:
        lastrequesttime = time.time() # Update time of last API call

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return { 'response error': response.text }

def __rate_limiter(self):
    """
    Waits until the required interval between API requests is reached
    """
    if lastrequesttime is not None: # If there was a previous call to the API
        timesince = time.time() - lastrequesttime
        if timesince < CALL_INTERVAL:
            time.sleep(CALL_INTERVAL - timesince)
