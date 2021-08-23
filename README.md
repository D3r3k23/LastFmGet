# LastFmGet

[![PyPI version](https://badge.fury.io/py/lastfmget.svg)](https://badge.fury.io/py/lastfmget)
[![Latest Release](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_release.yaml/badge.svg)](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_release.yaml)
[![Current Source](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_source.yaml/badge.svg)](https://github.com/D3r3k23/LastFmGet/actions/workflows/test_source.yaml)

Python package for accessing [Last.fm](https://www.last.fm) scrobble data using the public API.


## Installation
`pip install lastfmget`

### Dependencies
* requests
* requests_cache (Used only if set in api_cfg.yaml)
* pyyaml


## Usage

### Import
`import lastfmget`

### Config
`lastfmget.init('api_cfg.yaml')`

#### api_cfg.yaml example
```
api_url: http://ws.audioscrobbler.com/2.0/
api_key: <API KEY>
user_agent: <USER AGENT>
use_cache: true # true, false
call_rate: 5 # Calls per second
```

| Field      | Description                                                               |
|------------|---------------------------------------------------------------------------|
| api_url    | API root URL, should not be changed                                       |
| api_key    | Your private API key. See [here](https://www.last.fm/api#getting-started) |
| user_agent | Identifiable user agent for requests                                      |
| use_cache  | Use the functionality from requests_cache                                 |
| call_rate  | Max API requests per second                                               |

### Examples

#### Getting user information using the user.getInfo method
```
>>> info = lastfmget.user_info('D3r3k523')
>>> info['user']['playcount']
'159635'
>>> info['user']['url']
'https://www.last.fm/user/D3r3k523'
```

#### Getting a user's top 10 artists using the user.getTopArtists method
```
>>> artists = lastfmget.user_top_artists('D3r3k523', 10)
>>> [ artist['name'] for artist in artists['topartists']['artist'] ]
['Radiohead', 'Converge', 'Pink Floyd', 'Queens of the Stone Age', 'Bon Iver', 'Thee Oh Sees', 'Tame Impala', 'Arcade Fire', 'Mastodon', 'Beach House']
```

#### Example projects
* [LastFmTimeline](https://github.com/D3r3k23/LastFmTimeline)
* [PlaylistRanker](https://github.com/D3r3k23/PlaylistRanker)

### Details
* Provides functions for calling a specific Last.fm API method
* Gets a response from the API in JSON and returns a Python dictionary
* Data is stored as strings
* Errors

### Last.fm API methods available
* user.getInfo
* user.getRecentTracks
* user.getTopArtists
* user.getTopAlbums
* user.getTopTracks
* user.getWeeklyChartList
* user.getWeeklyArtistsChart
* user.getWeeklyAlbumsChart
* user.getWeeklyTracksChart

### Tips
* Use pprint on a response to see how the data is structured

### Last.fm API Reference
[Introduction](https://www.last.fm/api/intro)
