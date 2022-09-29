import random
import os
import colors


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def boat_check(y, x, boat_location_check):
    for i in range(3):
        boat_location_check.add(f'{[y - 1, x - 1 + i]}')
        boat_location_check.add(f'{[y, x + 1 - i]}')
        boat_location_check.add(f'{[y + 1, x - 1 + i]}')


def dots_near(y, x, boat_location):
    for i in range(3):
        if x - 1 + i in range(0, 10) and y - 1 in range(0, 10):
            boat_location[y - 1][x - 1 + i] = "•"
        if x + 1 - i in range(0, 10) and y in range(0, 10):
            boat_location[y][x + 1 - i] = "•"
        if x - 1 + i in range(0, 10) and y + 1 in range(0, 10):
            boat_location[y + 1][x - 1 + i] = "•"


def right_locate(board, boat_size, x, y):
    bool_check = True

    # Перевірка на можливість поставити корабель
    for i in range(boat_size):
        if f'[{y}, {x + i}]' in board.boats_zone_location:
            bool_check = False

    # Встановлення корабля вправо, якщо пройшло перевірку
    if bool_check:
        board.boats_location.append([])
        for i in range(boat_size):
            board.board_selections[y][x + i] = '⃞'
            board.boats_location[board.boards_number - 1].append((y, x + i))
            boat_check(y, x + i, board.boats_zone_location)
        board.boards_number += 1
        return bool_check


def down_locate(board, boat_size, x, y):
    bool_check = True

    # Перевірка на можливість поставити корабель
    for i in range(boat_size):
        if f'[{y + i}, {x}]' in board.boats_zone_location:
            bool_check = False

    # Встановлення корабля вниз, якщо пройшло перевірку
    if bool_check:
        board.boats_location.append([])
        for i in range(boat_size):
            board.board_selections[y + i][x] = '⃞'
            board.boats_location[board.boards_number - 1].append((y + i, x))
            boat_check(y + i, x, board.boats_zone_location)

        board.boards_number += 1
        return bool_check


def auto_locate(board, boat_size):
    b = 0
    while b != 1:
        right = random.randint(0, 1)
        if right == 1:
            x = random.randint(0, 9 - boat_size + 1)
            y = random.randint(0, 9)
            bool_check = right_locate(board, boat_size, x, y)
        else:
            x = random.randint(0, 9)
            y = random.randint(0, 9 - boat_size + 1)
            bool_check = down_locate(board, boat_size, x, y)

        if bool_check:
            b += 1


def coordinates_locate_check(board_num, boat_rotation, board):
    coordinates = input("Введіть координати: ")
    clear_screen()
    coordinates = coordinates.upper()
    if 3 >= len(coordinates) >= 2 \
            and coordinates[0] in board.letters_list \
            and coordinates[1:] in board.numbers_list:
        y = board.letters_list.index(coordinates[0])
        x = board.numbers_list.index(coordinates[1:])
        if boat_rotation == '1' and 10 - board_num >= x \
                and f'[{coordinates[0]}, {coordinates[1:]}]' \
                not in board.boats_zone_location:
            bool_check = right_locate(board, board_num, x, y)
            if not bool_check:
                clear_screen()
                print(colors.set_color("\nНе правильно введенні координати",
                                       colors.Color.red))
        elif boat_rotation == '2' and 10 - board_num >= y \
                and f'[{coordinates[0]}, {coordinates[1:]}]' \
                not in board.boats_zone_location:
            bool_check = down_locate(board, board_num, x, y)
            if not bool_check:
                clear_screen()
                print(colors.set_color("\nНе правильно введенні координати",
                                       colors.Color.red))
        else:
            clear_screen()
            print(colors.set_color("\nНе правильно введенні координати",
                                   colors.Color.red))
    else:
        clear_screen()
        print(colors.set_color("\nНе правильно введенні координати або "
                               "поворт корабля", colors.Color.red))
