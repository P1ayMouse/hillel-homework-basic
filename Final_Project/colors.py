class Color:
    yellow2 = '\033[1;35m'
    reset = '\033[0m'
    blue = '\033[0;34m'
    yellow = '\033[1;93m'
    red = '\033[1;93m'
    miss = '\033[0;37m'


def set_color(text, color):
    return color + text + Color.reset
