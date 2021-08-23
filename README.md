# LastFmGet

[![Unit Tests](https://github.com/D3r3k23/LastFmGet/actions/workflows/test.yaml/badge.svg)](https://github.com/D3r3k23/LastFmGet/actions/workflows/test.yaml)

API wrapper for accessing scrobble data from [Last.fm](https://www.last.fm).

### Installation

`pip install lastfmget`

### Example Usage


Import
```
import lastfmget
```
Config
```
lastfmget.init('api_cfg.yaml')
```
api_cfg.yaml example
```
api_url: http://ws.audioscrobbler.com/2.0/
api_key: <API KEY>
user_agent: <USER AGENT>
use_cache: true # true, false
call_rate: 5 # Calls per second
```
* api_url: API root URL, should not be changed
* api_key: Your private API key. See [here](https://www.last.fm/api#getting-started)
* user_agent: Use an identifiable user agent for requests
* user_cache: Use the functionality from requests_cache
* call_rate: Max API requests per second

Last.fm API Reference: [Introduction](https://www.last.fm/api/intro)
