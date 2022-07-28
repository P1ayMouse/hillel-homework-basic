year = int(input("Введіть рік: "))

if 1900 < year < 1_000_000:
    if year % 400 == 0:
        print(year, "рік є високосним")
    elif year % 100 == 0:
        print(year, "рік не є високосним")
    elif year % 4 == 0:
        print(year, "рік є високосним")
    else:
        print(year, "рік не є високосним")
else:
    print("Рік повинен бути в діапазоні від 1900 до 1000000")