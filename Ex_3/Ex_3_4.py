#1
#Calculating Factorial Number

n = 5
fact = 1

#calculate factorial
for i in range(1,n+1):
    fact = fact*i
print('The factorial of', n , 'is', fact)
print()#For space




#2
#Find prime number
    
#take input from keyboard
n = int(input('Enter a number: '))

#check number
if n>1:
    for i in range(2,n):
        if (n%i) == 0:
            print(n, 'is not a prime number')
            break
    else:
        print(n, 'is a prime number')
else:
    print(n, 'is not a prime number')
print()#For space




#3
#reverse the randaom entries

import random

num_list = []

#add number list
for i in range(20):
    x=random.randint(1, 100)
    num_list.append(x)


#method 2
# num_list = [random.randint(1,100) for a in range 20]

print(num_list)
print('Reverse list: ')
num_list.reverse()
print(num_list)
print()#For space




#4
#Count the vowels of the string

#input from keyboard
msg = str(input('Enter a string: '))
vowels = 'aeiou'
count = 0

#covert into lower case
msg = msg.lower()

#check the vowels
for x in msg:
    if x in vowels:
        count+=1

print('Vowels count is: ', count)

"""
#count the each vowels
vowels_count = {}
for x in vowels:
    count_v = msg.count(x)
    vowels_count[x] = count_v

counts = vowels_count.values()
total = sum(counts)

print('Vowel count is ', total)
print(vowels_count)
"""
print()#For space




#5
#Find all common character

#take input from keyboard
str1 = str(input('Enter 1st string: '))
str2 = str(input('Enter 2nd string: '))

#covert to lower case
str1 = str1.lower()
str2 = str2.lower()

#check all common character
my_str = ''           
for w in str1:
    if w in str2:
        my_str += w
print('Common characters:')
print(my_str)

"""
#check common charcter using set
result = list(set(str1) & set(str2))

print('Commmon characters: ')

for x in result:
    print(x)
"""
print()#For space




#6
#count total of even random numbers

import random

even_list = []

# print 20 even random numbers
for x in range(20):
    x=random.randrange(0,100,2) #will return a number of multiple of 5 between 1 and 100
    even_list.append(x)
    
#count total
total = sum(even_list)

print(even_list)
print('Total of the list: ' , total)
print()#For space




#7
#calculate average of random numbers

import random

#Generate 20 random numbers between 1 and 100
randomlist = random.sample(range(1, 100), 20)

#average
avg = sum(randomlist)/len(randomlist)

print(randomlist)
print('Random list average is ', round(avg,2))
print()#For space




#8
#Find prime numbers in random list

import random

#Generate rabdom number list
numlist = random.sample(range(0,2000),200)

primelist = []

#check number
for n in numlist: 
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                break
        else:
            primelist.append(n)

print(numlist)
print('Prime numbers:')
print(primelist)
print()#For space




#9
#Find odd numbers in random list

import random

#Generate random numbers
numlist = random.sample(range(0,100),20)

#filter odd number from random list
## method 1
oddlist1 = []

for x in numlist:
    if (x%2)!=0:
        oddlist1.append(x)
        
print(numlist)
print('Odd Numbers using method 1: ')
print(oddlist1)       

## method 2
oddlist2 = [x for x in numlist if (x%2)!=0]

print('Odd Numbers using method 2: ')
print(oddlist2)
            
## method 3
def check_odd(num):
    if (num%2)!=0:
        return True 

    return False 

#Extract elements from the numbers list
oddlist3 = list(filter(check_odd,numlist))

print('Odd Numbers using method 3: ')
print(oddlist3)
print()#For space




#10
#calculate factorial number for user input

#take input from keyboard
n = int(input('Enter a number: '))
fact = 1

#check the number
if n<0:
    print("Factorial doesn't exist for Negative number")
elif n==0:
    print('The factorial of 0 is 1')
else:
    for i in range(1,n+1):
        fact = fact*i
    print('The factorial of', n , 'is', fact)
