#remove 5th word

#remove word
with open('text.txt','r') as f:
    line = f.read().split()
    print('5th word:', line[4])
    del line[4]
    f.close()

#write again after removing
with open('text.txt','w') as f:
    for x in line:
        f.write(x + ' ')
    f.close()

#read file
f = open('text.txt', 'r')
print(f.read())
f.close()

