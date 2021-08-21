bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#print 2nd and 4th names
print('2nd name of cycle: ' , bicycles[1], '\n4th name of cycle: ', bicycles[3])

print()
#print the name which starts with 'r'
for x in bicycles:
        if x[0] == 'r':
            print(x)
