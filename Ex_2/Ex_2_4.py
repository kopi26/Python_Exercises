str1= 'Hello welcome to the python world!'

#length of string
length = len(str1)
print('Length of string: ' , length )


print()
#Print middle letter of string
if length % 2 == 0: #for even length string
    middle = length // 2
    print('Middle letters: ', str1[middle-1]+str1[middle])
else: 
    middle = length //2
    print('Middle letter: ', str1[middle])


print()
#Count letter in the string
count = 0
for x in str1:
    if x == 'o':
        count += 1
print('"O" letter count in the string:' , count)

