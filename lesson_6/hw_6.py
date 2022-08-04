len_str = 0

while len_str != 2:
    words = input("Enter words: ")
    len_str = len(words.split())

words = words[::-1]
words = words.title()
words_split = words.split()

first_word = words_split[0]
second_word = words_split[1]

print(second_word, first_word)