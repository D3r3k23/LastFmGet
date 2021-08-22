import lastfmget
import unittest

class Tests(unittest.TestCase):
    def test_assert(self):
        self.assertTrue(True)

    def test_nothing(self):sf
        self.assertFalse(False)

if __name__ == '__main__':
    lastfmget.init('test/api_cfg.yaml')
    unittest.main()
