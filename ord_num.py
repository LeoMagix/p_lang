#Ordinal numbers
ordinal = list(range(1, 10))
for numba in ordinal:
    if numba == 1:
        print(f'{numba}st')
    
    elif numba == 2:
        print(f'{numba}nd')
    
    elif numba == 3:
        print(f'{numba}rd')

    else:
        print(f'{numba}th')
