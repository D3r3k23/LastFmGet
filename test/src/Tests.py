import lastfmget
import unittest

user = 'D3r3k523'

class Tests:
    @staticmethod
    def run(cfg_fn):
        lastfmget.init(cfg_fn)
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests.TestCase)
        unittest.TextTestRunner().run(suite)

    class TestCase(unittest.TestCase):
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

        def test_user_weekly_chart_list_basic(self):
            chartlist = lastfmget.user_weekly_chart_list(user)
            self.assertEqual(chartlist['weeklychartlist']['@attr']['user'], user)

        def test_user_weekly_artist_chart_basic(self):
            artistchart = lastfmget.user_weekly_artist_chart(user)
            self.assertEqual(artistchart['weeklyartistchart']['@attr']['user'], user)

        def test_user_weekly_album_chart_basic(self):
            albumchart = lastfmget.user_weekly_album_chart(user)
            self.assertEqual(albumchart['weeklyalbumchart']['@attr']['user'], user)

        def test_user_weekly_track_chart_basic(self):
            trackchart = lastfmget.user_weekly_track_chart(user)
            self.assertEqual(trackchart['weeklytrackchart']['@attr']['user'], user)
