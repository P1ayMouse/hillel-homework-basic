def concatination(x, y):
    try:
        return x + y
    except TypeError:
        x = str(x)
        y = str(y)
        return x + y


if __name__ == "__main__":
    print(concatination(3, 5))
    print(concatination("Your number: ", 123))
