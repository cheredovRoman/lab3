import unittest
from logic import *

class TestGame(unittest.TestCase):

    def test_game_class_exists(self):
        self.assertTrue('Game' in globals())
    def test_generate_enemy_ships(self):
        self.assertEqual(generate_enemy_ships(), 0)

if __name__ == '__main__':
    unittest.main()