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
        suite  = unittest.defaultTestLoader.loadTestsFromTestCase(testcase)
        result = unittest.TextTestRunner().run(suite)
        results.append(result)

    return all(r.wasSuccessful() for r in results)

class RawMethodTests(unittest.TestCase):
    def test_user_info_basic(self):
        userinfo = lastfmget.user_info_raw(USER)
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
        userinfo     = lastfmget.user_info(USER)
        userinfo_raw = lastfmget.user_info_raw(USER)

        self.assertEqual(userinfo['name'],           userinfo_raw['user']['name'])
        self.assertEqual(userinfo['registered'], int(userinfo_raw['user']['registered']['unixtime']))

    def test_user_recent_tracks_compare_to_raw(self):
        recenttracks     = lastfmget.user_recent_tracks(USER, 25)
        recenttracks_raw = lastfmget.user_recent_tracks_raw(USER, limit=25)
        recenttracks_raw_filtered = [
            track for track in recenttracks_raw['recenttracks']['track']
            if not ('@attr' in track and track['@attr']['nowplaying'] == 'true')
        ]

        for track, track_raw in zip(recenttracks, recenttracks_raw_filtered):
            self.assertEqual(track['name'],   track_raw['name'])
            self.assertEqual(track['artist'], track_raw['artist']['#text'])

    def test_user_top_artists_compare_to_raw(self):
        topartists     = lastfmget.user_top_artists(USER, 25)
        topartists_raw = lastfmget.user_top_artists_raw(USER, limit=25)

        for artist, artist_raw in zip(topartists, topartists_raw['topartists']['artist']):
            self.assertEqual(artist['name'],          artist_raw['name'])
            self.assertEqual(artist['playcount'], int(artist_raw['playcount']))

    def test_user_top_albums_compare_to_raw(self):
        topalbums     = lastfmget.user_top_albums(USER, 25)
        topalbums_raw = lastfmget.user_top_albums_raw(USER, limit=25)

        for album, album_raw in zip(topalbums, topalbums_raw['topalbums']['album']):
            self.assertEqual(album['name'],          album_raw['name'])
            self.assertEqual(album['playcount'], int(album_raw['playcount']))

    def test_user_top_tracks_compare_to_raw(self):
        toptracks     = lastfmget.user_top_tracks(USER, 25)
        toptracks_raw = lastfmget.user_top_tracks_raw(USER, limit=25)

        for track, track_raw in zip(toptracks, toptracks_raw['toptracks']['track']):
            self.assertEqual(track['name'],          track_raw['name'])
            self.assertEqual(track['playcount'], int(track_raw['playcount']))

    def test_user_weekly_chart_list_compare_to_raw(self):
        chartlist     = lastfmget.user_weekly_chart_list(USER)
        chartlist_raw = lastfmget.user_weekly_chart_list_raw(USER)

        for chart, chart_raw in list(zip(chartlist, chartlist_raw['weeklychartlist']['chart']))[-1:-11:-1]:
            self.assertEqual(chart['start'], int(chart_raw['from']))
            self.assertEqual(chart['end'],   int(chart_raw['to']))

    def test_user_weekly_artist_chart_compare_to_raw(self):
        artistchart     = lastfmget.user_weekly_artist_chart(USER, None, None)
        artistchart_raw = lastfmget.user_weekly_artist_chart_raw(USER, start=None, end=None)

        self.assertEqual(artistchart['start'], int(artistchart_raw['weeklyartistchart']['@attr']['from']))
        self.assertEqual(artistchart['end'],   int(artistchart_raw['weeklyartistchart']['@attr']['to']))

        for artist, artist_raw in list(zip(artistchart['chart'], artistchart_raw['weeklyartistchart']['artist']))[:10]:
            self.assertEqual(artist['name'],          artist_raw['name'])
            self.assertEqual(artist['playcount'], int(artist_raw['playcount']))

    def test_user_weekly_album_chart_compare_to_raw(self):
        albumchart     = lastfmget.user_weekly_album_chart(USER, None, None)
        albumchart_raw = lastfmget.user_weekly_album_chart_raw(USER, start=None, end=None)

        self.assertEqual(albumchart['start'], int(albumchart_raw['weeklyalbumchart']['@attr']['from']))
        self.assertEqual(albumchart['end'],   int(albumchart_raw['weeklyalbumchart']['@attr']['to']))

        for album, album_raw in list(zip(albumchart['chart'], albumchart_raw['weeklyalbumchart']['album']))[:10]:
            self.assertEqual(album['name'],          album_raw['name'])
            self.assertEqual(album['playcount'], int(album_raw['playcount']))

    def test_user_weekly_track_chart_compare_to_raw(self):
        trackchart     = lastfmget.user_weekly_track_chart(USER, None, None)
        trackchart_raw = lastfmget.user_weekly_track_chart_raw(USER, start=None, end=None)

        self.assertEqual(trackchart['start'], int(trackchart_raw['weeklytrackchart']['@attr']['from']))
        self.assertEqual(trackchart['end'],   int(trackchart_raw['weeklytrackchart']['@attr']['to']))

        for track, track_raw in list(zip(trackchart['chart'], trackchart_raw['weeklytrackchart']['track']))[:10]:
            self.assertEqual(track['name'],          track_raw['name'])
            self.assertEqual(track['playcount'], int(track_raw['playcount']))

    def test_user_currently_playing_basic(self):
        nowplaying       = lastfmget.user_now_playing(USER)
        recenttracks_raw = lastfmget.user_recent_tracks_raw(USER)
        firsttrack = recenttracks_raw['recenttracks']['track'][0]

        if nowplaying is None:
            self.assertFalse('@attr' in firsttrack and firsttrack['@attr']['nowplaying'] == 'true')
        else:
            self.assertTrue('@attr' in firsttrack and firsttrack['@attr']['nowplaying'] == 'true')
            self.assertEqual(nowplaying['name'],   firsttrack['name'])
            self.assertEqual(nowplaying['artist'], firsttrack['artist']['#text'])

    def test_user_recent_tracks_for_now_playing(self):
        recenttracks = lastfmget.user_recent_tracks(USER, count=10)
        nowplaying   = lastfmget.user_now_playing(USER)

        if nowplaying is None:
            self.assertTrue(True)

        for track in recenttracks:
            self.assertFalse(track['name'] == nowplaying['name'] and track['artist'] == nowplaying['artist'])

    def test_user_recent_tracks_count(self):
        countvals = [ 1, 50, 199, 200, 201, 300 ] + random.choices(range(100, 501), k=3)
        for count in countvals:
            recenttracks = lastfmget.user_recent_tracks(USER, count=count)
            self.assertEqual(len(recenttracks), count)

    def test_user_top_artists_count(self):
        countvals = [ 1, 200, 499, 500, 501, 600 ] + random.choices(range(100, 1001), k=5)
        for count in countvals:
            topartists = lastfmget.user_top_artists(USER, count=count)
            self.assertEqual(len(topartists), count)

    def test_user_top_albums_count(self):
        countvals = [ 1, 200, 499, 500, 501, 600 ] + random.choices(range(100, 1001), k=5)
        for count in countvals:
            topalbums = lastfmget.user_top_albums(USER, count=count)
            self.assertEqual(len(topalbums), count)

    def test_user_top_tracks_count(self):
        countvals = [ 1, 200, 499, 500, 501, 600 ] + random.choices(range(100, 1001), k=5)
        for count in countvals:
            toptracks = lastfmget.user_top_tracks(USER, count=count)
            self.assertEqual(len(toptracks), count)

    def test_weekly_artist_chart_from_previous_week(self):
        chartlist  = lastfmget.user_weekly_chart_list(USER)
        randchart  = random.choice(chartlist[-10:-1])
        firstchart = chartlist[-1]

        randartistchart  = lastfmget.user_weekly_artist_chart(USER, randchart['start'],  randchart['end'])
        firstartistchart = lastfmget.user_weekly_artist_chart(USER, firstchart['start'], firstchart['end'])

        self.assertNotEqual(randartistchart['start'], firstartistchart['start'])
        self.assertNotEqual(randartistchart['end'],   firstartistchart['end'])

    def test_weekly_album_chart_from_previous_week(self):
        chartlist  = lastfmget.user_weekly_chart_list(USER)
        randchart  = random.choice(chartlist[-10:-1])
        firstchart = chartlist[-1]

        randalbumchart  = lastfmget.user_weekly_album_chart(USER, randchart['start'],  randchart['end'])
        firstalbumchart = lastfmget.user_weekly_album_chart(USER, firstchart['start'], firstchart['end'])

        self.assertNotEqual(randalbumchart['start'], firstalbumchart['start'])
        self.assertNotEqual(randalbumchart['end'],   firstalbumchart['end'])

    def test_weekly_track_chart_from_previous_week(self):
        chartlist  = lastfmget.user_weekly_chart_list(USER)
        randchart  = random.choice(chartlist[-10:-1])
        firstchart = chartlist[-1]

        randtrackchart  = lastfmget.user_weekly_track_chart(USER, randchart['start'],  randchart['end'])
        firsttrackchart = lastfmget.user_weekly_track_chart(USER, firstchart['start'], firstchart['end'])

        self.assertNotEqual(randtrackchart['start'], firsttrackchart['start'])
        self.assertNotEqual(randtrackchart['end'],   firsttrackchart['end'])

class ErrorTests(unittest.TestCase):
    def test_not_configured(self):
        lastfmget.core.ready = False
        with self.assertRaises(lastfmget.NotConfiguredError):
            lastfmget.user_info(USER)
        lastfmget.core.ready = True

    def test_user_not_found(self):
        with self.assertRaises(lastfmget.ParamError):
            lastfmget.user_info('ua26y7bv1gre2a4u9y54ob3vu3ab7vor9eav0o5ye')

    def test_invalid_params(self):
        with self.assertRaises(lastfmget.ParamError):
            lastfmget.user_recent_tracks_raw(USER, 2000)
