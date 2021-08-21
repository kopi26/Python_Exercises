a = [1, 4, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print('Less than 10 in the list')
for x in a:
    if x < 10:
        print(x)

print()

print('Odd numbers in the list')
for y in a:
    if y % 2 != 0:
        print(y)

print()

print('Even numbers in the list')
for z in a:
    if z % 2 == 0:
        print(z)
