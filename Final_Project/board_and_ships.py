import locate
import shoot
import random
import simple_colors as color


class Board:
    def __init__(self):
        self.board_selections = [[" " for _ in range(10)]
                                 for _ in range(10)]
        self.attack_board = [["⃞" for _ in range(10)]
                             for _ in range(10)]
        self.boards_number = 1
        self.letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.boats_zone_location = set()
        self.scores = 0
        self.boats_location = []
        self.dict_boats = {}

    # Дошка із кораблями
    def draw_board_selections(self):
        # Вивід чисел
        print(f"{' ':^3}", end="")
        for i in range(len(self.numbers_list)):
            print(self.numbers_list[i], end=f"{' ':^3}")
        print()

        # Вивід поля
        for i in range(len(self.board_selections)):
            print(self.letters_list[i], end=f"{' ':^2}")  # Вивід букв
            for j in range(len(self.board_selections[0])):
                print(self.board_selections[i][j], end=f"{' ':^3}")
            print()
        print()

    # Дошка для демонстрації атак гравця
    def draw_attack_board(self):
        # Вивід чисел
        print(f"{' ':^3}", end="")
        for i in range(len(self.numbers_list)):
            print(self.numbers_list[i], end=f"{' ':^3}")
        print()

        # Вивід поля
        for i in range(len(self.attack_board)):
            print(self.letters_list[i], end=f"{' ':^2}")  # Вивід букв
            for j in range(len(self.attack_board[0])):
                print(self.attack_board[i][j], end=f"{' ':^3}")
            print()
        print()


# Автоматичне виставлення кораблів
def auto_ship_locate(obj_name):
    locate.auto_locate(obj_name, 1)
    locate.auto_locate(obj_name, 1)
    locate.auto_locate(obj_name, 1)
    locate.auto_locate(obj_name, 1)
    locate.auto_locate(obj_name, 2)
    locate.auto_locate(obj_name, 2)
    locate.auto_locate(obj_name, 2)
    locate.auto_locate(obj_name, 3)
    locate.auto_locate(obj_name, 3)
    locate.auto_locate(obj_name, 4)


# Ввод гравця
def player_enter():
    if_auto = input("\t1. Автоматично\n\t2. Самоввід\n\nВідповідь: ")
    locate.clear_screen()
    board_type = 0
    while True:
        if if_auto == "1":
            auto_ship_locate(player_board)
            break
        elif if_auto == "2":
            if player_board.boards_number == 11:
                locate.clear_screen()
                break
            player_board.draw_board_selections()
            print("\t1. Корабель праворуч\n\t2. Корабель вниз\n")
            rotation = input("Відповідь: ")
            if player_board.boards_number <= 4:
                board_type = 1
            elif 5 <= player_board.boards_number <= 7:
                board_type = 2
            elif 8 <= player_board.boards_number <= 9:
                board_type = 3
            elif player_board.boards_number == 10:
                board_type = 4
            locate.coordinates_locate_check(board_type, rotation, player_board)
        else:
            locate.clear_screen()
            print(color.yellow("\nНе правильно введена відповідь\n"))
            if_auto = input("\t1. Автоматично\n\t2. Самоввід\n\nВідповідь: ")
            locate.clear_screen()


# Віднесення кожної палуби, до її корабля
def dict_in_dict(board):
    duplicate_dict = board.dict_boats.copy()
    for i in range(1, len(duplicate_dict) + 1):
        for j in range(len(duplicate_dict[i])):
            if type(board.dict_boats[i]) == dict:
                board.dict_boats[i].update({duplicate_dict[i][j]: 1})
            else:
                board.dict_boats[i] = {duplicate_dict[i][j]: 1}


if __name__ == "__main__":
    bot_board = Board()
    auto_ship_locate(bot_board)
    player_board = Board()
    player_enter()
    player_board.dict_boats = dict(zip([i for i in range(1, 11)],
                                       player_board.boats_location))
    dict_in_dict(player_board)
    bot_board.dict_boats = dict(zip([i for i in range(1, 11)],
                                    bot_board.boats_location))
    dict_in_dict(bot_board)
    player_bool_shoot = True
    bot_bool_shoot = False
    while True:
        bot_board.draw_board_selections()
        bot_board.draw_attack_board()
        player_board.draw_board_selections()
        print("\033[0;34m" f"\t\tРахунок" f"\n\tГравець: {player_board.scores}"
              f"\tБот: {bot_board.scores}" "\033[0m")
        # Стрільба гравця
        if player_bool_shoot:
            coordinates = input("\nВведіть координати: ")
            coordinates = coordinates.upper()
            if 3 >= len(coordinates) >= 2 \
                    and coordinates[0] in player_board.letters_list \
                    and coordinates[1:] in player_board.numbers_list:
                y = player_board.letters_list.index(coordinates[0])
                x = player_board.numbers_list.index(coordinates[1:])
                locate.clear_screen()
                player_bool_shoot = shoot.shot(bot_board, y, x,
                                               bot_board.attack_board)
                bot_bool_shoot = not player_bool_shoot
            else:
                locate.clear_screen()
                player_bool_shoot = True
                bot_bool_shoot = not player_bool_shoot
                print(color.yellow("\nНе правильно введенні координати"))
        # Стрільба бота
        if bot_bool_shoot:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            bot_bool_shoot = shoot.shot(player_board, y, x,
                                        player_board.board_selections)
            player_bool_shoot = not bot_bool_shoot
            locate.clear_screen()
        # Перемога гравця
        if player_board.scores == 10:
            locate.clear_screen()
            bot_board.draw_attack_board()
            player_board.draw_board_selections()
            print(color.green(f"\n{'Ви перемогли!':>30}"))
            break
        # Перемога бота
        if bot_board.scores == 10:
            locate.clear_screen()
            bot_board.draw_attack_board()
            player_board.draw_board_selections()
            print(color.red(f"\n{'Переміг бот!':>30}"))
            break
