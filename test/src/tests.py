import lastfmget
import unittest

class Tests(unittest.TestCase):
    def test_assert(self):
        self.assertTrue(True)

    def test_nothing(self):
        self.assertFalse(False)

    def test_user_info(self):
        r = lastfmget.user_info('D3r3k523')
        print(r)

if __name__ == '__main__':
    lastfmget.init('test/api_cfg.yaml')
    unittest.main()
