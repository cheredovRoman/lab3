import random
def generate_enemy_ships(size, fill):
    if size == 0:
        return 0
    enemy_ships = [[fill for i in range(size)] for i in range(size)]
    return enemy_ships