import lastfmget
import unittest

def run(cfg_fn):
    lastfmget.init(cfg_fn)
    unittest.main()

class Tests(unittest.TestCase):
    def test_assert(self):
        self.assertTrue(True)

    def test_nothing(self):
        self.assertFalse(False)

    def test_api_call(self):
        r = lastfmget.user_info('D3r3k523')
        self.assertEqual(r['user']['name'], 'D3r3k523')
