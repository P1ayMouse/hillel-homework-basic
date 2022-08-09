input_numbers = input("Write your numbers: ")
input_index = int(input("Write index: "))
i = 0

numbers_list = input_numbers.split()

while i != len(numbers_list[input_index:]):
    numbers_list[input_index - 1 + i] = numbers_list[input_index + i]
    i += 1

numbers_list.pop()

print(numbers_list)
