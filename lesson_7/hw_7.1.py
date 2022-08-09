input_numbers = input("Write your numbers: ")
input_index = int(input("Write index: "))
insert_number = int(input("Insert number: "))

i = 1

numbers_list = input_numbers.split()
numbers_list.append('0')

while i != len(numbers_list[input_index:]) + 1:
    numbers_list[-i] = numbers_list[-i - 1]
    i += 1

numbers_list[input_index] = insert_number

print(numbers_list)
