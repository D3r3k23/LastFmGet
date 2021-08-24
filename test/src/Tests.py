import lastfmget
import unittest
import sys

user = 'D3r3k523'

class Tests(unittest.TestCase):
    @staticmethod
    def run_all(cfg_fn):
        lastfmget.init(cfg_fn)
        unittest.main(argv=[sys.argv[0]])

    def test_user_info_basic(self):
        userinfo = lastfmget.user_info(user)
        self.assertEqual(userinfo['user']['name'], user)

    def test_user_recent_tracks_basic(self):
        recenttracks = lastfmget.user_recent_tracks(user)
        self.assertEqual(recenttracks['recenttracks']['@attr']['user'], user)

    def test_user_top_artists_basic(self):
        topartists = lastfmget.user_top_artists(user)
        self.assertEqual(topartists['topartists']['@attr']['user'], user)

    def test_user_top_albums_basic(self):
        topalbums = lastfmget.user_top_albums(user)
        self.assertEqual(topalbums['topalbums']['@attr']['user'], user)

    def test_user_top_tracks_basic(self):
        toptracks = lastfmget.user_top_tracks(user)
        self.assertEqual(toptracks['toptracks']['@attr']['user'], user)
