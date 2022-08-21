planetarium_circus = {i for i in range(1, 5)}
planetarium_stadium = {i for i in range(5, 5 + 3)}
circus_stadium = {i for i in range(8, 8 + 1)}

illness = {i for i in range(35, 35 + 3)}
planetarium = {i for i in range(16, 16 + 19)}
circus = {i for i in range(6, 6 + 10)}
stadium = {i for i in range(1, 6)}

print(len((planetarium | circus | stadium | illness) - (planetarium_circus | planetarium_stadium | circus_stadium)))