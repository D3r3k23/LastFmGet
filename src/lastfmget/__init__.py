"""
Python package for accessing Last.fm scrobble data using the public API.

### Github
`https://github.com/D3r3k23/LastFmGet/`

### Install
`pip install lastfmget`

### Import
`import lastfmget`

### Configure
`init('api_cfg.yaml')`

### Methods
`lastfmget.methods`
"""
from .core import init
from .methods import *
from .raw_methods import *

from .errors import (
    LastFmGetError,
    NotConfiguredError,
    LastFmError,
    ParamError,
    ApiKeyError,
    OfflineError,
    RateLimitError
)
