##read n lines of file

#get no of lines
n = int(input('Enter no of lines: '))

#read file
with open('test.txt','r') as f:
    lines = f.readlines()
    
    #read first n lines
    print(f'First {n} lines:')
    read_lines = ''.join(lines[:n])
    print(read_lines)
    
    #read last n lines
    print(f'Last {n} lines:')
    read_lines = ''.join(lines[-n:])
    print(read_lines)
    f.close()



##read particular lines and save as another

#read file
with open('test.txt','r') as f:
    lines = f.readlines()
    extract_lines = ''.join(lines[2:5])
    f.close()

#save in to another file
with open('test_copy.txt','w') as f:
    f.write(extract_lines)
    f.close()

#read file
f = open('test_copy.txt', 'r')
print(f.read())
f.close()
    
    
