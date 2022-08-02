input_number = int(input("Enter number: "))
yes = False

while input_number > 9:
    unmodul_number = input_number // 10
    modul_number = input_number % 10
    input_number //= 10
    while unmodul_number != 0:
        if modul_number == unmodul_number % 10:
            print("Yes")
            yes = True
        unmodul_number //= 10

if yes != True:
    print("No")