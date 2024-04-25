import random

# функция генерации кораблей
def generate_enemy_ships(size, fill):
    if size == 0:
        return 0
    enemy_ships = [[fill for i in range(size)] for i in range(size)]

    return enemy_ships


def generate_ships(ships, s_x, s_y, ship_len1, ship_len2, ship_len3):
    global enemy_ships
    ships_list = []
    # генерируем список случайных длин кораблей
    for i in range(0, ships):
        ships_list.append(random.choice([ship_len1, ship_len2, ship_len3]))
    #print(ships_list)

    # подсчет суммарной длины кораблей
    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0

    while sum_1_enemy != sum_1_all_ships:
        # обнуляем массив кораблей врага
        enemy_ships = [[0 for i in range(s_x + 1)] for i in
                       range(s_y + 1)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника

        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = random.randrange(1, 3)  # 1- горизонтальное 2 - вертикальное

            primerno_x = random.randrange(0, s_x)
            if primerno_x + len > s_x:
                primerno_x = primerno_x - len

            primerno_y = random.randrange(0, s_y)
            if primerno_y + len > s_y:
                primerno_y = primerno_y - len

            # print(horizont_vertikal, primerno_x,primerno_y)
            if horizont_vertikal == 1:
                if primerno_x + len <= s_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y][primerno_x + j] = i + 1  # записываем номер корабля
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= s_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            # print(check_near_ships)
                            if check_near_ships == 0:  # записываем в том случае, если нет ничего рядом
                                enemy_ships[primerno_y + j][primerno_x] = i + 1  # записываем номер корабля
                        except Exception:
                            pass

        # делаем подсчет 1
        sum_1_enemy = 0
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1

        # print(sum_1_enemy)
        # print(ships_list)
        # print(enemy_ships)
        return enemy_ships


def count_ships(board):
    count = 0
    if board == 0:
        return count
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                # Check if this is a new ship
                if (i == 0 or board[i - 1][j] == 0) and (j == 0 or board[i][j - 1] == 0):
                    count += 1
    return count


def check_winner(x, y, enemy_ships, boom):
    win = False
    if enemy_ships[y][x] > 0:
        boom[y][x] = enemy_ships[y][x]
    sum_enemy_ships = sum(sum(i) for i in zip(*enemy_ships))
    sum_boom = sum(sum(i) for i in zip(*boom))
    if sum_enemy_ships == sum_boom:
        win = True
    return win

def score(board):
    """
    Функция принимает на вход игровое поле board и возвращает количество очков,
    заработанных игроком
    """
    count4 = 0
    count3 = 0
    count2 = 0
    score = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 4:
                count4 += 1
                score += 1
            if board[i][j] == 3:
                count3 += 1
                score += 1
            if board[i][j] == 2:
                count2 += 1
                score += 1
            if board[i][j] == 1:
                score += 2
            if (count4 % 4) == 0 & count4 != 0:
                score += 1
            if (count3 % 3) == 0 & count3 != 0:
                score += 2
            if (count2 % 2) == 0 & count2 != 0:
                score += 3
            print(score)
    return score





