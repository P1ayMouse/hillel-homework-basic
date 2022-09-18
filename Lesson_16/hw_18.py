import random


class Board:
    def __init__(self):
        self.board_selections = [["⃞️" for _ in range(10)] for _ in range(10)]
        self.letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.boats_location = set()

    def draw_board(self):
        print("    1   2   3   4   5   6   7   8   9   10")

        for i in range(len(self.board_selections)):
            print(self.letters_list[i], end="\t")
            for j in range(len(self.board_selections[0])):
                print(self.board_selections[i][j], end="\t")
            print()


def boat_check(y, x, boat_location_check):
    for i in range(3):
        boat_location_check.add(f'{[y - 1, x - 1 + i]}')
        boat_location_check.add(f'{[y, x + 1 - i]}')
        boat_location_check.add(f'{[y + 1, x - 1 + i]}')
    return boat_location_check


# def bot():
#     bot_board = Board()
#     bot_board.draw_board()
#     boats = set()
#
#     b = 0
#     while b < 4:
#         location_x = random.randint(0, 9)
#         location_y = random.randint(0, 9)
#         if f'[{location_y}, {location_x}]' not in boats:
#             bot_board.board_selections[location_y][location_x] = '⬜'
#             boats = boat_check(location_y, location_x, boats)
#             b += 1
#
#     b = 0
#     while b < 1:
#         location_x = random.randint(0, 9)
#         location_y = random.randint(0, 6)
#         bool_check = True
#
#         for i in range(4):
#             if f'[{location_y + i}, {location_x}]' in boats:
#                 bool_check = False
#
#         if bool_check == True:
#             for j in range(4):
#                 bot_board.board_selections[location_y + j][location_x] = '⬜'
#                 boats = boat_check(location_y + j, location_x, boats)
#                 b += 1
#     bot_board.draw_board()


def right_locate(board, boat_size):
    bool_check = True

    location_x = random.randint(0, 9 - boat_size + 1)
    location_y = random.randint(0, 9)

    for i in range(boat_size):
        if f'[{location_y}, {location_x + i}]' in board.boats_location:
            bool_check = False

    if bool_check:
        for i in range(boat_size):
            board.board_selections[location_y][location_x + i] = '⬜'
            board.boats_location = boat_check(location_y, location_x + i,
                                              board.boats_location)
        return bool_check


def left_locate(board, boat_size):
    bool_check = True

    location_x = random.randint(0, 9)
    location_y = random.randint(0, 9 - boat_size + 1)

    for i in range(boat_size):
        if f'[{location_y + i}, {location_x}]' in board.boats_location:
            bool_check = False

    if bool_check:
        for i in range(boat_size):
            board.board_selections[location_y + i][location_x] = '⬜'
            board.boats_location = boat_check(location_y + i, location_x,
                                                board.boats_location)
        return bool_check


def locate(board, boat_size):
    b = 0
    while b != 1:
        right = random.randint(0, 1)
        if right == 1:
            bool_check = right_locate(board, boat_size)
        else:
            bool_check = left_locate(board, boat_size)

        if bool_check:
            b += 1


if __name__ == "__main__":
    bot_board = Board()
    bot_board.draw_board()
    locate(bot_board, 1)
    locate(bot_board, 1)
    locate(bot_board, 1)
    locate(bot_board, 1)
    locate(bot_board, 2)
    locate(bot_board, 2)
    locate(bot_board, 2)
    locate(bot_board, 3)
    locate(bot_board, 3)
    locate(bot_board, 4)
    bot_board.draw_board()
