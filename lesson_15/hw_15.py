def concatination(x, y):
    try:
        xy = x + y
        return xy
    except TypeError:
        x = str(x)
        y = str(y)
        xy = x + y
        return xy


if __name__ == "__main__":
    print(concatination(3, 5))
    print(concatination("Your number: ", 123))
