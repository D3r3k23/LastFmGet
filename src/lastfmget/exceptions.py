from enum import Enum

class LastFmErrorCodes(Enum):
    InvalidApiKey = 10
    Offline = 11
    RateLimit = 29


class LastFmGetError(Exception):
    def __init__(self, msg='Generic lastfmget error'):
        super().__init__(msg)

class NotConfiguredError(LastFmGetError):
    def __init__(self):
        super().__init__('lastfmget not configured')


class LastFmError(LastFmGetError):
    def __init__(self, msg='Generic Last.fm error'):
        super().__init__(msg)

class ApiKeyError(LastFmError):
    def __init__(self):
        super().__init__('Invalid API key provided')

class OfflineError(LastFmError):
    def __init__(self):
        super().__init__('Last.fm is offline')

class RateLimitError(LastFmError):
    def __init__(self):
        super().__init__('Last.fm API rate limit exceeded')
