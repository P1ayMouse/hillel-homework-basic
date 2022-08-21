newspapers = {75}
magazines = {27}

print(sum(i - 13 for i in (newspapers | magazines)) + 13)
