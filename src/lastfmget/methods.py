"""
Methods for getting formatted data from Last.fm.
"""
from .raw_methods import *

def user_info(user):
    """
    Gets info about a user.

    Arguments:
      * user (str) -- username

    Returns:
    ```
      {
        'name' (str) -- username
        'playcount' (int) -- number of scrobbles
        'registered' (int) -- registration date Unix timestamp
        'url' (str) -- user's Last.fm URL
      }
    ```
    """
    raw = user_info_raw(user)
    userinfo = raw['user']

    return {
        'name'       : str(userinfo['name']),
        'playcount'  : int(userinfo['playcount']),
        'registered' : int(userinfo['registered']['unixtime']),
        'url'        : str(userinfo['url'])
    }

def user_currently_playing(user, count=50):
    """
    Gets the user's currently playing track.

    Arguments:
      * user (str) -- username

    Returns:
    ```
      None if no track playing, else:
      {
        'name' (str) -- track name
        'artist' (str) -- artist name
        'album' (str) -- album name
      }
    ```
    """
    track = user_recent_tracks_raw(user, limit=10)['recenttracks']['track'][0]
    if __is_now_playing(track):
        return {
            'name'   : str(track['name']),
            'artist' : str(track['artist']['#text']),
            'album'  : str(track['album']['#text'])
        }
    else:
        return None

def user_recent_tracks(user, count=50):
    """
    Gets the user's recent tracks.

    * Excludes currently playing tracks

    Arguments:
      * user (str) -- username
      * count (int) -- number of tracks

    Returns:
    ```
      [
        {
          'name' (str) -- track name
          'artist' (str) -- artist name
          'album' (str) -- album name
          'date' (int or None) -- date Unix timestamp - None if track is now playing
        }
      ]
    ```
    """
    MAX_PER_PAGE = 200

    numpages = (count + MAX_PER_PAGE - 1) // MAX_PER_PAGE
    numtracksinlastpage = count - (numpages - 1) * MAX_PER_PAGE

    tracks = []
    for pagenum in range(1, numpages + 1):
        numtracksinpage = (MAX_PER_PAGE if pagenum < numpages else numtracksinlastpage)
        raw = user_recent_tracks_raw(user, limit=numtracksinpage, page=pagenum)
        page = raw['recenttracks']['track']

        for track in page:
            if not __is_now_playing(track):
                tracks.append({
                    'name'   : str(track['name']),
                    'artist' : str(track['artist']['#text']),
                    'album'  : str(track['album']['#text']),
                    'date'   : int(track['date']['uts'])
                })
    return tracks

def user_top_artists(user, count=50, period=None):
    """
    Gets the user's top artists.

    Arguments:
      * user (str) -- username
      * count (int) -- number of artists
      * period (str) -- time period [overall, 7day, 1month, 3month, 6month, 12month]

    Returns:
    ```
      [
        {
          'name' (str) -- artist name
          'rank' (int) -- ranking
          'playcount' (int) -- number of scrobbles
        }
      ]
    ```
    """
    MAX_PER_PAGE = 500
    numpages = (count + MAX_PER_PAGE - 1) // MAX_PER_PAGE
    numartistsinlastpage = count - (numpages - 1) * MAX_PER_PAGE

    artists = []
    for i in range(1, numpages + 1):
        numartistsinpage = numartistsinlastpage if i == numpages else MAX_PER_PAGE
        raw = user_top_artists_raw(user, limit=numartistsinpage, page=i, period=period)
        page = raw['topartists']['artist']

        for artist in page:
            artists.append({
                'name'      : str(artist['name']),
                'rank'      : int(artist['@attr']['rank']),
                'playcount' : int(artist['playcount'])
            })
    return artists

def user_top_albums(user, count=50, period=None):
    """
    Gets the user's top albums.

    Arguments:
      * user (str) -- username
      * count (int) -- number of albums
      * period (str) -- time period [overall, 7day, 1month, 3month, 6month, 12month]

    Returns:
    ```
      [
        {
          'name' (str) -- album name
          'artist' (str) -- artist name
          'rank' (int) -- ranking
          'playcount' (int) -- number of scrobbles
        }
      ]
    ```
    """
    MAX_PER_PAGE = 500
    numpages = (count + MAX_PER_PAGE - 1) // MAX_PER_PAGE
    numalbumsinlastpage = count - (numpages - 1) * MAX_PER_PAGE

    albums = []
    for i in range(1, numpages + 1):
        numalbumsinpage = numalbumsinlastpage if i == numpages else MAX_PER_PAGE
        raw = user_top_albums_raw(user, limit=numalbumsinpage, page=i, period=period)
        page = raw['topalbums']['album']

        for album in page:
            albums.append({
                'name'      : str(album['name']),
                'artist'    : str(album['artist']['name']),
                'rank'      : int(album['@attr']['rank']),
                'playcount' : int(album['playcount'])
            })
    return albums

def user_top_tracks(user, count=50, period=None):
    """
    Gets the user's top tracks.

    Arguments:
      * user (str) -- username
      * count (int) -- number of tracks
      * period (str) -- time period [overall, 7day, 1month, 3month, 6month, 12month]

    Returns:
    ```
      [
        {
          'name' (str) -- track name
          'artist' (str) -- artist name
          'rank' (int) -- ranking
          'playcount' (int) -- number of scrobbles
          'duration' (int) -- track duration (seconds)
        }
      ]
    ```
    """
    MAX_PER_PAGE = 500
    numpages = (count + MAX_PER_PAGE - 1) // MAX_PER_PAGE
    numtracksinlastpage = count - (numpages - 1) * MAX_PER_PAGE

    tracks = []
    for i in range(1, numpages + 1):
        numtracksinpage = numtracksinlastpage if i == numpages else MAX_PER_PAGE
        raw = user_top_tracks_raw(user, limit=numtracksinpage, page=i, period=period)
        page = raw['toptracks']['track']

        for track in page:
            tracks.append({
                'name'      : str(track['name']),
                'artist'    : str(track['artist']['name']),
                'rank'      : int(track['@attr']['rank']),
                'playcount' : int(track['playcount']),
                'duration'  : int(track['duration'])
            })
    return tracks

def user_weekly_chart_list(user):
    """
    Gets a list of the user's available charts.

    * Chart is defined by a date range
    * For use by chart methods

    Arguments:
      * user (str) -- username

    Returns:
    ```
      [
        {
          'start' (int) -- chart start Unix timestamp
          'end' (int) -- chart end Unix timestamp
        }
      ]
    ```
    """
    raw = user_weekly_chart_list_raw(user)
    charts = raw['weeklychartlist']['chart']

    return [
        {
            'start' : int(chart['from']),
            'end'   : int(chart['to'])
        }
        for chart in charts
    ]

def user_weekly_artist_chart(user, start=None, end=None):
    """
    Gets the user's artist chart for the given date range.

    * Should use timestamps generated by user_weekly_chart_list
    * Can omit end
    * Default is latest chart
    * Timestamps of returned chart may differ from arguments

    Arguments:
      * user (str) -- username
      * start (int) -- chart start Unix timestamp
      * end (int) -- chart end Unix timestamp

    Returns:
    ```
      {
        'start' (int) -- chart start Unix timestamp
        'end' (int) -- chart end Unix timestamp
        'chart': [
          {
            'name' (str) -- artist name
            'rank' (int) -- chart rank
            'playcount' (int) -- number of scrobbles in chart
          }
        ]
      }
    ```
    """
    raw = user_weekly_artist_chart_raw(user, start=start, end=end)
    start       = raw['weeklyartistchart']['@attr']['from']
    end         = raw['weeklyartistchart']['@attr']['to']
    artistchart = raw['weeklyartistchart']['artist']

    return {
        'start' : int(start),
        'end'   : int(end),
        'chart' : [
            {
                'name'      : str(artist['name']),
                'rank'      : int(artist['@attr']['rank']),
                'playcount' : int(artist['playcount'])
            }
            for artist in artistchart
        ]
    }

def user_weekly_album_chart(user, start=None, end=None):
    """
    Gets the user's album chart for the given date range.

    * Should use timestamps generated by user_weekly_chart_list
    * Can omit end
    * Default is latest chart
    * Timestamps of returned chart may differ from arguments

    Arguments:
      * user (str) -- username
      * start (int) -- chart start Unix timestamp
      * end (int) -- chart end Unix timestamp

    Returns:
    ```
      {
        'start' (int) -- chart start Unix timestamp
        'end' (int) -- chart end Unix timestamp
        'chart': [
          {
            'name' (str) -- album name
            'artist' (str) -- artist name
            'rank' (int) -- chart rank
            'playcount' (int) -- number of scrobbles in chart
          }
        ]
      }
    ```
    """
    raw = user_weekly_album_chart_raw(user, start=start, end=end)
    start      = raw['weeklyalbumchart']['@attr']['from']
    end        = raw['weeklyalbumchart']['@attr']['to']
    albumchart = raw['weeklyalbumchart']['album']

    return {
        'start' : int(start),
        'end'   : int(end),
        'chart' : [
            {
                'name'      : str(album['name']),
                'artist'    : str(album['artist']['#text']),
                'rank'      : int(album['@attr']['rank']),
                'playcount' : int(album['playcount'])
            }
            for album in albumchart
        ]
    }

def user_weekly_track_chart(user, start=None, end=None):
    """
    Gets the user's track chart for the given date range.

    * Should use timestamps generated by user_weekly_chart_list
    * Can omit end
    * Default is latest chart
    * Timestamps of returned chart may differ from arguments

    Arguments:
      * user (str) -- username
      * start (int) -- chart start Unix timestamp
      * end (int) -- chart end Unix timestamp

    Returns:
    ```
      {
        'start' (int) -- chart start Unix timestamp
        'end' (int) -- chart end Unix timestamp
        'chart': [
          {
            'name' (str) -- track name
            'artist' (str) -- artist name
            'rank' (int) -- chart rank
            'playcount' (int) -- number of scrobbles in chart
          }
        ]
      }
    ```
    """
    raw = user_weekly_track_chart_raw(user, start=start, end=end)
    start      = raw['weeklyalbumchart']['@attr']['from']
    end        = raw['weeklyalbumchart']['@attr']['to']
    trackchart = raw['weeklytrackchart']['track']

    return {
        'start' : int(start),
        'end'   : int(end),
        'chart' : [
            {
                'name'      : str(trackchart['name']),
                'artist'    : str(trackchart['artist']['#text']),
                'rank'      : int(trackchart['@attr']['rank']),
                'playcount' : int(trackchart['playcount'])
            }
            for trackchart in trackchart
        ]
    }

def __is_now_playing(track):
    """
    Returns True if the track is now playing.
    """
    return '@attr' in track and track['@attr']['nowplaying'] == 'true'
