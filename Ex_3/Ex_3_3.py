#1
for i in range(10):
    for j in range(i+1):
        print('*', end='')
    print()
print()#For space



#2
for i in range(10):
    for j in range(10-i):
        print('*', end='')
    print()
print()#For space



#3
for i in range(10):
    print('square of ', i, ' is ', (i**2))
print()#For space



#4
for i in range(10):
    for j in range(10-i):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()
print()#For space



#5
for i in range(10):
    for j in range(10-i):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()
print()#For space



#6
for i in range(9,-1,-1):
    for j in range(10-i):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()
print()#For space



