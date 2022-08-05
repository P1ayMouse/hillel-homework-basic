input_string = input("Enter words: ")
input_char = input("Enter char: ")

chars_number = 0
char_number_check = input_string.find(input_char)
i = 0

len_input_string = len(input_string)

while i != len_input_string:
    i += 1
    find_input_char = input_string.find(input_char, i)

    if char_number_check != find_input_char:
        char_number_check = find_input_char
        chars_number += 1

if chars_number == 0:
    print("Char not found")
else:
    print("Char count in string: ", chars_number)