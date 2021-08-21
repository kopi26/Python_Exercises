#read file
with open('notes.txt', 'r') as f:
    marks = [float(x) for x in f.read().split()]
    print(marks)
    f.close()

#calculate average
avg = sum(marks)/len(marks)
print(f'Average is: {avg:.2f}')


##rewrite with marks rating
with open('notes2.txt', 'a') as f:
    for x in marks:
        if x >= 10:
            f.write(str(x) + ' admitted' + '\n')
        else:
            f.write(str(x) + ' failed' + '\n')
    f.close()


#read file
f=open('notes2.txt', 'r')
print(f.read())
f.close()
    
