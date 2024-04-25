import unittest
from logic import *
from game import draw_point
from game import check_winner

class TestGame(unittest.TestCase):

    # def test_game_class_exists(self):
    #     self.assertTrue('logic' in globals())
    def test_generate_enemy_ships(self):
        self.assertEqual(generate_enemy_ships(0, 0), 0)

    def test_generate_enemy_ships_size_5(self):
        enemy_ships = [[0 for i in range(5)] for i in range(5)]
        self.assertEqual(generate_enemy_ships(5, 0), enemy_ships)

    def test_generate_enemy_ships(self):
        enemy_ships = [[0 for i in range(5)] for i in range(5)]
        self.assertEqual(generate_enemy_ships(5, 0), enemy_ships)

        # def test_draw_point(self):
        #     self.assertEqual(draw_point(1, 1), 1)

    def test_check_winner_false(self):
        self.assertFalse(check_winner(1, 1), False)

    def test_check_winner_true(self):
        self.assertTrue(check_winner(1, 1), True)


if __name__ == '__main__':
    unittest.main()