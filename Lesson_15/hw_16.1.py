def longest_words(file):
    file_reader = open(file, "r")
    words_list = file_reader.read().split()
    len_word = 0
    max_len_word = []
    # for i in range(len(words_list)):
    #     for j in range(len(words_list)):
    #         if words_list[i] > words_list[j] and words_list[i] > max_len_word:
    #             max_len_word = words_list[i]
    for i in range(len(words_list)):
        if len(words_list[i]) > len_word:
            len_word = len(words_list[i])

    for j in range(len(words_list)):
        if len(words_list[j]) == len_word:
            max_len_word.append(words_list[j])
    file_reader.close()
    return max_len_word


if __name__ == "__main__":
    file_name = "article.txt"
    for word in range(len(longest_words(file_name))):
        print(longest_words(file_name)[word])
