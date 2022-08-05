number = int(input("Enter number: "))
one = "1"

if 3 > number or number > 9:
    print("The number must be between 3 and 9")
else:
    number_list = list(range(1, number + 1))
    number_str = str(number_list)
    number_str = ''.join(number_str)
    number_str = number_str.strip("[]")
    number_str = number_str.replace(", ", "")

    print(one)
    for i in number_list[:-1]:
        print(number_str[:i] + number_str[i::-1])
        i += 1

    print("\n" + one.center(number * 2 - 1))
    for i in number_list[:-1]:
        print((number_str[:i] + number_str[i::-1]).center(number * 2 - 1))
        i += 1

    print("\n" + one.rjust(number * 2 - 1))
    for i in number_list[:-1]:
        print((number_str[:i] + number_str[i::-1]).rjust(number * 2 - 1))
        i += 1
