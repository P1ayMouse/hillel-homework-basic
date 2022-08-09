input_numbers_one = input("Write your numbers: ")
input_numbers_two = input("Write your numbers: ")
unique_numbers = 0

numbers_list_one = input_numbers_one.split()
numbers_list_two = input_numbers_two.split()

all_of_numbers_list = numbers_list_one + numbers_list_two

for i in all_of_numbers_list:
    count = 0
    for j in all_of_numbers_list:
        if i == j:
            count += 1
    if count == 1:
        unique_numbers += 1

print("Unique numbers:", unique_numbers)
