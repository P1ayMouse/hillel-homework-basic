natural_number = 1000
n = 0

while n < 1000:
    n += 1
    result = n * n

    count = 1
    i = n
    while i > 0:
        i //= 10
        count *= 10

    modul_result = result % count
    if modul_result == n:
        print(n, "*", n, "=", n * n)

