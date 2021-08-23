import lastfmget
import unittest
import sys

class Tests(unittest.TestCase):
    @staticmethod
    def run_all(cfg_fn):
        lastfmget.init(cfg_fn)
        unittest.main(argv=[sys.argv[0]])

    def test_assert(self):
        self.assertTrue(True)

    def test_nothing(self):
        self.assertFalse(False)

    def test_api_call(self):
        r = lastfmget.user_info('D3r3k523')
        self.assertEqual(r['user']['name'], 'D3r3k523')
