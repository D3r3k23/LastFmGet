# LastFmGet

[![PyPI version](https://badge.fury.io/py/lastfmget.svg)](https://pypi.org/project/lastfmget)
[![Latest Release](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_release.yaml/badge.svg)](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_release.yaml)
[![Current Source](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_source.yaml/badge.svg)](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_source.yaml)


**NOTE: This package is still in early development and is not fully tested. I made this just to use in a few of my own projects, so the interface may change according to my needs. If anyone wants to use the package, please let me know in the Discussions page.**

LastFmGet is a Python package for accessing [Last.fm](https://www.last.fm) scrobble data using the public API.

* Provides functions for calling specific Last.fm API methods
* Must use a cfg YAML file and call lastfmget.init() before any API calls
* Gets a response from the API in JSON and returns a Python dictionary
* Use _raw method verions for more direct access to the Last.fm API


## Installation
`pip install lastfmget`

### Dependencies
* **Python3**
* requests
* requests_cache (used only if configured in api_cfg.yaml)
* pyyaml


## Documentation
### [lastfmget](https://raw.githack.com/D3r3k23/LastFmGet/master/docs/pdoc/lastfmget.html)


## Usage

### Import
`import lastfmget`

### Config
`lastfmget.init('api_cfg.yaml')`

#### api_cfg.yaml example ([data/example_api_cfg.yaml](https://github.com/D3r3k23/LastFmGet/blob/master/data/example_api_cfg.yaml))
```
api_url: http://ws.audioscrobbler.com/2.0/
api_key: <API KEY>
user_agent: <USER AGENT>
call_rate: 5 # Calls per second
cache:
  enable: true
  dir: .cache
  backend: sqlite
  lifetime: 120 # Seconds
# or (defaults)
cache:
  enable: true
# or (disable)
cache:
  enable: false
```

| Field      | Description                                                 |
|------------|-------------------------------------------------------------|
| api_url    | API root URL, should be 'http://ws.audioscrobbler.com/2.0/' |
| api_key    | Your private API key. See [here](https://www.last.fm/api)   |
| user_agent | Identifiable user agent for requests                        |
| call_rate  | Max API requests per second                                 |
| cache      | enable: use requests_cache<br>dir: (optional) cache location<br>backend: (optional) sqlite recommended<br>lifetime: (optional) expire_after time in seconds |

### Code Examples

#### Getting user information using the user.getInfo method
```
>>> info = lastfmget.user_info('D3r3k523')
>>> info['playcount']
159635
>>> info['user']['url']
'https://www.last.fm/user/D3r3k523'
```

#### Getting a user's top 10 artists using the user.getTopArtists method
```
>>> topartists = lastfmget.user_top_artists('D3r3k523', 10)
>>> [ artist['name'] for artist in topartists ]
['Radiohead', 'Converge', 'Pink Floyd', 'Queens of the Stone Age', 'Bon Iver', 'Thee Oh Sees', 'Tame Impala', 'Arcade Fire', 'Mastodon', 'Beach House']
```

### Example Projects
* [LastFmTimeline](https://github.com/D3r3k23/LastFmTimeline)
* [PlaylistRanker](https://github.com/D3r3k23/PlaylistRanker)
* [Tests](https://github.com/D3r3k23/LastFmGet/blob/master/test/test/tests.py)


## Last.fm API Methods Available
| Function                           | Last.fm API method        |
|------------------------------------|---------------------------|
| lastfmget.user_info                | user.getInfo              |
| lastfmget.user_recent_tracks       | user.getRecentTracks      |
| lastfmget.user_top_artists         | user.getTopArtists        |
| lastfmget.user_top_albums          | user.getTopAlbums         |
| lastfmget.user_top_tracks          | user.getTopTracks         |
| lastfmget.user_weekly_chart_list   | user.getWeeklyChartList   |
| lastfmget.user_weekly_artist_chart | user.getWeeklyArtistChart |
| lastfmget.user_weekly_album_chart  | user.getWeeklyAlbumChart  |
| lastfmget.user_weekly_track_chart  | user.getWeeklyTrackChart  |


## Last.fm API Reference
* ### [Introduction](https://www.last.fm/api/intro)
* ### [Terms of Service](https://www.last.fm/api/tos)
