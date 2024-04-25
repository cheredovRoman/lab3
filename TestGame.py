import unittest
from game import *

class TestGame(unittest.TestCase):

    def test_game_class_exists(self):
        self.assertTrue('Game' in globals())
    def test_draw_table(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()