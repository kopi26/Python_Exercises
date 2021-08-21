#swap 3rd and 2nd line

#swap the lines
with open('test.txt','r') as f:
    line = f.read().splitlines()
    line[1],line[2] = line[2],line[1]
    f.close()

#write again after removing
with open('test.txt','w') as f:
    for x in line:
        f.write(x + '\n')
    f.close()

#read file
f = open('test.txt', 'r')
print(f.read())
f.close()
