"""
Thin wrappers around Last.fm API methods.

* Module generated by gen_raw_methods_module.py from methods.yaml
"""
from .core import __get_response

def user_info_raw(user):
    """user.getInfo"""
    payload = {
        'method' : 'user.getInfo',
        'user'   : user
    }
    return __get_response(payload)

def user_recent_tracks_raw(user, limit=50, page=1):
    """user.getRecentTracks"""
    payload = {
        'method' : 'user.getRecentTracks',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_top_artists_raw(user, limit=50, page=1, period=None):
    """user.getTopArtists"""
    payload = {
        'method' : 'user.getTopArtists',
        'user'   : user,
        'limit'  : limit,
        'page'   : page,
        'period' : period
    }
    return __get_response(payload)

def user_top_albums_raw(user, limit=50, page=1, period=None):
    """user.getTopAlbums"""
    payload = {
        'method' : 'user.getTopAlbums',
        'user'   : user,
        'limit'  : limit,
        'page'   : page,
        'period' : period
    }
    return __get_response(payload)

def user_top_tracks_raw(user, limit=50, page=1, period=None):
    """user.getTopTracks"""
    payload = {
        'method' : 'user.getTopTracks',
        'user'   : user,
        'limit'  : limit,
        'page'   : page,
        'period' : period
    }
    return __get_response(payload)

def user_weekly_chart_list_raw(user):
    """user.getWeeklyChartLIst"""
    payload = {
        'method' : 'user.getWeeklyChartLIst',
        'user'   : user
    }
    return __get_response(payload)

def user_weekly_artist_chart_raw(user, start=None, end=None):
    """user.getWeeklyArtistChart"""
    payload = {
        'method' : 'user.getWeeklyArtistChart',
        'user'   : user,
        'from'   : start,
        'to'     : end
    }
    return __get_response(payload)

def user_weekly_album_chart_raw(user, start=None, end=None):
    """user.getWeeklyAlbumChart"""
    payload = {
        'method' : 'user.getWeeklyAlbumChart',
        'user'   : user,
        'from'   : start,
        'to'     : end
    }
    return __get_response(payload)

def user_weekly_track_chart_raw(user, start=None, end=None):
    """user.getWeeklyTrackChart"""
    payload = {
        'method' : 'user.getWeeklyTrackChart',
        'user'   : user,
        'from'   : start,
        'to'     : end
    }
    return __get_response(payload)
