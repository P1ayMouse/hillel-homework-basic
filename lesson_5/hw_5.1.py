natural_number = 1000
n = 0

while n < 1000:
    n += 1
#    print(n)
    result = n * n
    while result > 0:
        modul_result = result % 10
#        print(modul_result)
        result //= 10
#        print(result)
        if modul_result == n:
            print(n, "*", n, "=", n * n)
