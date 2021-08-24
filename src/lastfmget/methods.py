from .core import __get_response

def user_info(user):
    """ user.getInfo """

    payload = {
        'method' : 'user.getInfo',
        'user'   : user
    }
    return __get_response(payload)

def user_recent_tracks(user, limit=50, page=1):
    """ user.getRecentTracks """

    payload = {
        'method' : 'user.getRecentTracks',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_top_artists(user, limit=50, page=1):
    """ user.getTopArtists """

    payload = {
        'method' : 'user.getTopArtists',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_top_albums(user, limit=50, page=1):
    """ user.getTopAlbums """

    payload = {
        'method' : 'user.getTopAlbums',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_top_tracks(user, limit=50, page=1):
    """ user.getTopTracks """

    payload = {
        'method' : 'user.getTopTracks',
        'user'   : user,
        'limit'  : limit,
        'page'   : page
    }
    return __get_response(payload)

def user_weekly_chart_list(user):
    """ user.getWeeklyChartLIst """

    payload = {
        'method' : 'user.getWeeklyChartLIst',
        'user'   : user
    }
    return __get_response(payload)

def user_weekly_artist_chart(user, start=0, end=0):
    """ user.getWeeklyArtistChart """

    payload = {
        'method' : 'user.getWeeklyArtistChart',
        'user'   : user,
        'start'  : start,
        'end'    : end
    }
    return __get_response(payload)

def user_weekly_album_chart(user, start=0, end=0):
    """ user.getWeeklyAlbumChart """

    payload = {
        'method' : 'user.getWeeklyAlbumChart',
        'user'   : user,
        'start'  : start,
        'end'    : end
    }
    return __get_response(payload)

def user_weekly_track_chart(user, start=0, end=0):
    """ user.getWeeklyTrackChart """

    payload = {
        'method' : 'user.getWeeklyTrackChart',
        'user'   : user,
        'start'  : start,
        'end'    : end
    }
    return __get_response(payload)
