import unittest
import random
import inspect
import sys

import lastfmget

random.seed()

USER = 'D3r3k523'

def run(cfg_fn):
    lastfmget.init(cfg_fn)

    testcases = [ cls for _, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass)
        if issubclass(cls, unittest.TestCase)
    ]

    results = []
    for testcase in testcases:
        print(f'Running TestCase: {testcase.__name__}')
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(testcase)
        result = unittest.TextTestRunner().run(suite)
        results.append(result)

    return all(r.wasSuccessful() for r in results)

class RawMethodTests(unittest.TestCase):
    def test_user_info_basic(self):
        userinfo = lastfmget.user_info_raw(USER)
        self.assertTrue(False)
        self.assertEqual(userinfo['user']['name'], USER)

    def test_user_recent_tracks_basic(self):
        recenttracks = lastfmget.user_recent_tracks_raw(USER)
        self.assertEqual(recenttracks['recenttracks']['@attr']['user'], USER)

    def test_user_top_artists_basic(self):
        topartists = lastfmget.user_top_artists_raw(USER)
        self.assertEqual(topartists['topartists']['@attr']['user'], USER)

    def test_user_top_albums_basic(self):
        topalbums = lastfmget.user_top_albums_raw(USER)
        self.assertEqual(topalbums['topalbums']['@attr']['user'], USER)

    def test_user_top_tracks_basic(self):
        toptracks = lastfmget.user_top_tracks_raw(USER)
        self.assertEqual(toptracks['toptracks']['@attr']['user'], USER)

    def test_user_weekly_chart_list_basic(self):
        chartlist = lastfmget.user_weekly_chart_list_raw(USER)
        self.assertEqual(chartlist['weeklychartlist']['@attr']['user'], USER)

    def test_user_weekly_artist_chart_basic(self):
        artistchart = lastfmget.user_weekly_artist_chart_raw(USER)
        self.assertEqual(artistchart['weeklyartistchart']['@attr']['user'], USER)

    def test_user_weekly_album_chart_basic(self):
        albumchart = lastfmget.user_weekly_album_chart_raw(USER)
        self.assertEqual(albumchart['weeklyalbumchart']['@attr']['user'], USER)

    def test_user_weekly_track_chart_basic(self):
        trackchart = lastfmget.user_weekly_track_chart_raw(USER)
        self.assertEqual(trackchart['weeklytrackchart']['@attr']['user'], USER)

class MethodTests(unittest.TestCase):
    def test_user_info_compare_to_raw(self):
        userinforaw = lastfmget.user_info_raw(USER)
        userinfo    = lastfmget.user_info(USER)
        self.assertEqual(userinfo['name'], userinforaw['user']['name'])

    def test_user_recent_tracks_count_with_now_playing(self):
        countvals = [ 1, 50, 200, 300 ] + random.choices(range(100, 501), k=3)
        for count in countvals:
            recenttracks = lastfmget.user_recent_tracks(USER, count=count)
            self.assertEqual(len(recenttracks), count)

    # def test_user_recent_tracks_basic(self):
    #     recenttracksraw = lastfmget.user_recent_tracks_raw(user)
    #     recenttracks    = lastfmget.user_recent_tracks(user)
    #     self.assertEqual(recenttracks['recenttracks']['@attr']['user'], user)

    # def test_user_top_artists_basic(self):
    #     topartists = lastfmget.user_top_artists(user)
    #     self.assertEqual(topartists['topartists']['@attr']['user'], user)

    # def test_user_top_albums_basic(self):
    #     topalbums = lastfmget.user_top_albums(user)
    #     self.assertEqual(topalbums['topalbums']['@attr']['user'], user)

    # def test_user_top_tracks_basic(self):
    #     toptracks = lastfmget.user_top_tracks(user)
    #     self.assertEqual(toptracks['toptracks']['@attr']['user'], user)

    # def test_user_weekly_chart_list_basic(self):
    #     chartlist = lastfmget.user_weekly_chart_list(user)
    #     self.assertEqual(chartlist['weeklychartlist']['@attr']['user'], user)

    # def test_user_weekly_artist_chart_basic(self):
    #     artistchart = lastfmget.user_weekly_artist_chart(user)
    #     self.assertEqual(artistchart['weeklyartistchart']['@attr']['user'], user)

    # def test_user_weekly_album_chart_basic(self):
    #     albumchart = lastfmget.user_weekly_album_chart(user)
    #     self.assertEqual(albumchart['weeklyalbumchart']['@attr']['user'], user)

    # def test_user_weekly_track_chart_basic(self):
    #     trackchart = lastfmget.user_weekly_track_chart(user)
    #     self.assertEqual(trackchart['weeklytrackchart']['@attr']['user'], user)
