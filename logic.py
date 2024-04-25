import random
def generate_enemy_ships(size):
    if size == 0:
        return 0
    enemy_ships = [[0 for i in range(size)] for i in range(size)]
    return enemy_ships