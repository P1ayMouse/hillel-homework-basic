import locate
import simple_colors as color


# Відзначення підбитої палуби
def attack_boat_search(board, cords, attack_board):
    """
    :param board: Дошка
    :param cords: Координати, у яку йде стрільба
    :param attack_board: Дошка, де будуть відзначатися влучання
    """
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
                                     attack_board)
                for c in range(len(cords_list)):
                    attack_board[cords_list[c][0]][cords_list[c][1]] = "✘"


# Стрільба у певну координату
def shot(player_1, player_2, y, x, attack_board):
    """
    :param player_1: Той, у кого стіляють
    :param player_2: Той, хто стріляє
    :param y: Буква
    :param x: Цифра
    :param attack_board: Дошка, де будуть відзначатися влучання
    :return: Якщо влучив, або не правильно вказана координата - дається
    додатковий хід
    """
    if attack_board[y][x] != "•" \
            and attack_board[y][x] != "✘":
        if player_1.board_selections[y][x] == "⃞":
            attack_board[y][x] = "✘"
            player_2.scores += 1
            attack_boat_search(player_1, (y, x), attack_board)
            return True
        if player_1.board_selections[y][x] == " ":
            attack_board[y][x] = "•"
            return False
    else:
        print(color.yellow("\nНе правильно введенні координати"))
        return True
