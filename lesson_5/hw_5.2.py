summ = 0
count = -1
max = 0
min = 0
pair = 0
not_pair = 0

while True:
    input_number = int(input("Enter number: "))
    if min == 0:
        min = input_number
    count += 1
    if input_number == 0:
        print("Сума чисел:", summ)
        print("Cереднє арифметичне чисел:", summ / count)
        print("Мінімальне число:", min, "Максимальне число:", max)
        print("Кількість парних чисел:", pair, "Кількість не парних чисел:", not_pair)
        break
    else:
        summ += input_number
        if max < input_number:
            max = input_number
        if min > input_number:
            min = input_number
        if input_number % 2 == 0:
            pair += 1
        if input_number % 2 != 0:
            not_pair += 1