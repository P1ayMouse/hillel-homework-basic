def table(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        n = list(n)
        n.sort()
        print(" ̲" + "＿" * 3 + "＿" + "＿" * 8 + "＿" + "＿" * 5 + " ̲")
        for i in n:
            print("⎢" + str(i) + " " * (5 - len(str(i))) + "⎪" + f'{("Кратне 3" + " " * 5) if i % 3 == 0 else ("Не кратне 3" + " " * 2)}' + "⎪" + f'{"Парне     " if i % 2 == 0 else "Не парне  "}' + "⎥")
        print("—" + "⎯" * 3 + "⎯" + "⎯" * 8 + "⎯" + "⎯" * 5 + "—")
        return n
    return wrapper


@table
def numbers(number):
    import random
    random_numbers = set(random.randint(1, 100) for i in range(number))
    return random_numbers

numbers(10)
