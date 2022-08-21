newspapers = {i for i in range(27, 75 + 27)}
magazines = {i for i in range(13, 27 + 13)}
newspapers_magazines = {i for i in range(1, 13)}

print(len((newspapers | magazines) - newspapers_magazines))

