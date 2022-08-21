badges_stamps = {i for i in range(1, 16)}
stamps = {i for i in range(16, 35)}
badges = {i for i in range(35, 23 + 35 - 16)}
schoolchild = {i for i in range(1, 52)}

print(len(schoolchild - (badges_stamps | stamps | badges)))
