import locate


def attack_boat_search(board, cords):
    check_zero = 0
    for i in range(1, len(board.dict_boats) + 1):
        if cords in board.dict_boats[i]:
            board.dict_boats[i].update({cords: 0})
            values_list = list(board.dict_boats[i].values())
            for j in range(len(values_list)):
                if values_list[j] == 0:
                    check_zero += 1
            if check_zero == len(values_list):
                cords_list = list(board.dict_boats[i].keys())
                for dots in range(len(cords_list)):
                    locate.dots_near(cords_list[dots][0], cords_list[dots][1],
                                     board.attack_board)
                for c in range(len(cords_list)):
                    board.attack_board[cords_list[c][0]][cords_list[c][1]] = "✘"


def shot(player_1, player_2, cords):
        y = player_1.letters_list.index(cords[0])
        x = player_1.numbers_list.index(cords[1:])
        if player_2.attack_board[y][x] != "•" \
                and player_2.attack_board[y][x] != "✘":
            if player_2.board_selections[y][x] == "⃞":
                player_2.attack_board[y][x] = "✘"
                attack_boat_search(player_2, (y, x))
                player_1.scores += 1
            if player_2.board_selections[y][x] == " ":
                player_2.attack_board[y][x] = "•"
