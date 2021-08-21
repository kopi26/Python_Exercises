a = [60, 55, 65, 80, 75, 68, 93, 72]

tot = 0
#calculating sum 
# tot = sum(a)

#calulating sum of elements
for x in a:
    tot += x 

#calculating average
avg = tot/len(a)
print('Average is: ', avg)


print()

if avg > 70:
    print('Selected for next level')
else:
    print('Not selected for next level')
