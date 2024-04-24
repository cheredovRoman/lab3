import unittest
from game import Game

class TestGame(unittest.TestCase):

    def test_game_class_exists(self):
        self.assertTrue('Game' in globals())

if __name__ == '__main__':
    unittest.main()