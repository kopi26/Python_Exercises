#insert line in given position

#get line position and sentence
position = int(input('Enter line position as number: '))
new_line = str(input('Enter the line: '))

#insert new line at given position
with open('test.txt', 'r') as f:
    lines = f.readlines()
    lines.insert(position-1, new_line+'\n')
    f.close()

with open('test.txt', 'w') as f:
    lines = ''.join(lines)
    f.write(lines)
    f.close()

#read file
f = open('test.txt', 'r')
print(f.read())
f.close()
