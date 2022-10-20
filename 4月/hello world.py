for m in range(1, 10):
    for n in range(1, m+1):
        print(f'{m} * {n} = {m * n}', end=' ')
    print()

m = 1
while m <= 9:
    n = 1
    while n <= m:
        print(f'{m} * {n} = {m * n}', end=' ')
        n += 1
    print()
    m += 1

m = 1
while m <=9:
    for n in range(1, m+1):
        print(f'{m} * {n} = {m*n}', end=' ')
    print()
    m += 1

for m in range(1, 10):
    n = 1
    while n <= m:
        print(f'{m} * {n} = {m*n}', end=' ')
        n += 1
    print()
