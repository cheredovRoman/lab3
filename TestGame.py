import unittest
from logic import *

class TestGame(unittest.TestCase):

    # def test_game_class_exists(self):
    #     self.assertTrue('logic' in globals())
    def test_generate_enemy_ships(self):
        self.assertEqual(generate_enemy_ships(), 0)

    def test_generate_enemy_ships_size_5(self):
        enemy_ships = [[0 for i in range(5)] for i in range(5)]
        self.assertEqual(generate_enemy_ships(), enemy_ships)

if __name__ == '__main__':
    unittest.main()