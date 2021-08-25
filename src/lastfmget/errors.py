from enum import Enum

class LastFmErrorCodes(Enum):
    """Last.fm response error codes."""
    InvalidParams = 6
    InvalidApiKey = 10
    Offline = 11
    RateLimit = 29


class LastFmGetError(Exception):
    """Generic lastfmget error."""
    def __init__(self, msg='Generic lastfmget error'):
        """Calls Exception(msg)"""
        super().__init__(msg)

class NotConfiguredError(LastFmGetError):
    """lastfmget not configured - must call lastfmget.init() first."""
    def __init__(self, msg='lastfmget not configured'):
        """Calls LastFmGetError(msg)"""
        super().__init__(msg)

class LastFmError(LastFmGetError):
    """Generic Last.fm response error."""
    def __init__(self, msg='Generic Last.fm response error'):
        """Calls LastFmGetError(msg)"""
        super().__init__(msg)

class ParamError(LastFmError):
    """Invalid parameters provideded - example: user not found."""
    def __init__(self, msg):
        """Calls LastFmError(msg)"""
        super().__init__(msg)

class ApiKeyError(LastFmError):
    """Last.fm API key is invalid."""
    def __init__(self, msg='Invalid API key provided'):
        """Calls LastFmError(msg)"""
        super().__init__(msg)

class OfflineError(LastFmError):
    """Last.fm offline."""
    def __init__(self, msg='Last.fm is offline'):
        """Calls LastFmError(msg)"""
        super().__init__(msg)

class RateLimitError(LastFmError):
    """Last.fm API rate limit exceeded - decrease api_cfg.call_rate."""
    def __init__(self, msg='Last.fm API rate limit exceeded'):
        """Calls LastFmError(msg)"""
        super().__init__(msg)
