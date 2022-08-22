book_A = {i for i in range(25-10)}
book_B = {i for i in range(15, 15 + 22 - 10)}
book_C = {i for i in range(27, 27 + 22 - 10)}

book_A_B = {i for i in range(33)}
book_A_C = {i for i in range(64, 64 + 32)}
book_B_C = {i for i in range(33, 33 + 31)}



print("Only A and B:", len(book_A_B - (book_A | book_B)))
print("Only A and C:", len(book_A_C - (book_A | book_C)))
print("Only B and C:", len((book_B | book_C) - book_B_C))

#print("Only A:", len((book_A_B | book_A_C | book_A_B_C) - book_A))