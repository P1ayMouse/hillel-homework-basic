def simple_numbers(x, y):
    for i in range(x, y):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

for n in simple_numbers(1, 100):
    if n >= 2:
        print(n, end=" ")
