import lastfmget
import unittest

class Tests(unittest.TestCase):
    def test_print(self):
        print('Hi')
        self.assertTrue(True)

if __name__ == '__main__':
    lastfmget.init('test/api_cfg.yaml')
    unittest.main()
