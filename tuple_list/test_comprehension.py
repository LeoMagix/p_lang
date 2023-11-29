odd_num = []
for odd in range(20):
    if odd % 2 == 1:
        odd_num.append(odd)
print(odd_num)

list_odd = [odd for odd in range(22) if odd % 2 == 1]
print(list_odd)

even_num = [even for even in range(22) if even % 2 != 1]
print(even_num)


