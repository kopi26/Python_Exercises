#write in to file
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#write into file
f = open('doc1.txt','w')
for x in color:
    f.write(x + '\n')   
f.close()

#read file
f = open('doc1.txt', 'r')
print(f.read())
f.close()
