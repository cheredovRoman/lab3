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
        list1 = [
            [3, 5, 7],
            [2, 4, 6],
            [1, 8, 9]
        ]
        list2 = [
            [3, 5, 7],
            [2, 1, 6],
            [1, 8, 9]
        ]
        self.assertFalse(check_winner(1, 2, list1, list2), False))
    def test_check_winner_true(self):
        list1 = [
            [3, 5, 7],
            [2, 4, 6],
            [1, 8, 9]
        ]
        list2 = [
            [3, 5, 7],
            [2, 4, 6],
            [1, 8, 9]
        ]
        self.assertTrue(check_winner(1, 1, list1, list2), True)

    def test_count_ship(self):
        self.assertEqual(count_ship(board), 0)


if __name__ == '__main__':
    unittest.main()