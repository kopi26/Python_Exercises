#replace the line from file

#replace line
with open('test.txt', 'r') as f:
    lines = f.read().splitlines()
    lines[2] = 'sorry! The content of this line has been changed!'
    f.close()

#write again after replacing sentence
with open('test.txt','w') as f:
    for x in lines:
        f.write(x + '\n')
    f.close()

#read file
f = open('test.txt', 'r')
print(f.read())
f.close()
