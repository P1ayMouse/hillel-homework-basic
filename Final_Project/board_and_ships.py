import locate
import colors


class Board:
    def __init__(self):
        self.board_selections = [["⃞️" for _ in range(10)]
                                 for _ in range(10)]
        self.attack_board = [["⃞️" for _ in range(10)]
                             for _ in range(10)]
        self.boards_number = 1
        self.letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.boats_zone_location = set()
        self.scores = 0
        # self.boats_location = []

    def draw_board_selections(self):
        # Вивід чисел
        print("\n\t", end="")
        for i in range(len(self.numbers_list)):
            print(self.numbers_list[i], end="\t")
        print()

        # Вивід поля
        for i in range(len(self.board_selections)):
            print(self.letters_list[i], end="\t")  # Вивід букв
            for j in range(len(self.board_selections[0])):
                print(self.board_selections[i][j], end="\t")
            print()
        print()

    def draw_attack_board(self):
        # Вивід чисел
        print("\n\t", end="")
        for i in range(len(self.numbers_list)):
            print(self.numbers_list[i], end="\t")
        print()

        # Вивід поля
        for i in range(len(self.attack_board)):
            print(self.letters_list[i], end="\t")  # Вивід букв
            for j in range(len(self.attack_board[0])):
                print(self.attack_board[i][j], end="\t")
            print()
        print()


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
    locate.auto_locate(obj_name, 4)  # board.boards_type.append(boat_size)


def player_enter():
    if_auto = input("\t1. Автоматично\n\t2. Самоввід\n\nВідповідь: ")
    locate.clear_screen()
    board_type = 0
    while True:
        if if_auto == "1":
            auto_ship_locate(player_board)
            bot_board.draw_attack_board()
            player_board.draw_board_selections()
            break
        elif if_auto == "2":
            if player_board.boards_number == 11:
                player_board.draw_board_selections()
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
            print(colors.set_color("\nНе правильно введена відповідь\n",
                                   colors.Color.red))
            if_auto = input("\t1. Автоматично\n\t2. Самоввід\n\nВідповідь: ")


def shot():
    while player_board.scores != 20:
        print(f"{'Рахунок':^90}", f"{f'Гравець: {player_board.scores}':^50}", f"{f'Бот: {bot_board.scores}'}")
        coordinates = input("\nВведіть координати: ")
        locate.clear_screen()
        coordinates = coordinates.upper()
        coordinates_index_let = player_board.letters_list.index(coordinates[0])
        coordinates_index_num = player_board.numbers_list.index(coordinates[1:])
        if 3 >= len(coordinates) >= 2 \
                and coordinates[0] in player_board.letters_list \
                and coordinates[1:] in player_board.numbers_list \
                and bot_board.attack_board[coordinates_index_let] \
            [coordinates_index_num] != "•" \
                and bot_board.attack_board[coordinates_index_let] \
            [coordinates_index_num] != "✘":
            if bot_board.board_selections[coordinates_index_let][coordinates_index_num] == "⬜":
                bot_board.attack_board[coordinates_index_let][coordinates_index_num] = "✘"
                player_board.scores += 1
            elif bot_board.board_selections[coordinates_index_let][coordinates_index_num] == "⃞️":
                bot_board.attack_board[coordinates_index_let][coordinates_index_num] = "•"
            else:
                print("Невідома помилка")
        else:
            locate.clear_screen()
            print(colors.set_color("\nНе правильно введенні координати",
                                   colors.Color.red))
        bot_board.draw_board_selections()
        bot_board.draw_attack_board()
        player_board.draw_board_selections()


if __name__ == "__main__":
    bot_board = Board()
    auto_ship_locate(bot_board)
    player_board = Board()
    player_enter()
    shot()
