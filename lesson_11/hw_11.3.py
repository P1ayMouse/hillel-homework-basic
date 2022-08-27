def table(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        n = list(n)
        n.sort()
        print("⎯" * 18)
        for i in n:
            print("⎢" + f'{str(i):>4}' + "⎪" + f'{"Кратне 3" if i % 3 == 0 else "Не кратне 3":>12}' + "⎪" +
                  f'{"Парне" if i % 2 == 0 else "Не парне":>10}' + "⎥")
        print("⎯" * 18)
        return n

    return wrapper


@table
def numbers(number):
    import random
    random_numbers = set(random.randint(1, 100) for i in range(number))
    return random_numbers


numbers(10)
