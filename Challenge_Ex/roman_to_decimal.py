###1
#Find closet number pair

import random

def find_diff(num):
    count = len(num)
    x,y = 0,1
    short_diff = abs(num[x] - num[y])

    #find closet pair
    for i in range(count):
        for j in range(count):
            if(j==i):
                continue
            diff = abs(num[i] - num[j])
            if short_diff > diff:
                short_diff = diff
                x,y = i,j

    #print closet pair            
    print(num[x],num[y])



#Random numbers
r  = random.sample(range(1,100),10)
print(r)
find_diff(r)





###2
#Convert Roman to Decimal

def roman_to_decimal(roman):
    values = {
        'I' :   1,
        'V' :   5,
        'X' :   10,
        'L' :   50,
        'C' :   100,
        'D' :   500,
        'M' :   1000
        }

    count = len(roman)
    pre_roman = 0
    decimal = 0

    for i in range(count-1,-1,-1):
        if values[roman[i]] >= pre_roman:
            #larger than previous
            decimal += values[roman[i]]
        else:
            #smaller than previous
            decimal -= values[roman[i]]

        #update the previous roman 
        pre_roman = values[roman[i]]

    #print decimal value
    print(decimal)

    


roman_to_decimal('IX')
roman_to_decimal('IV')
roman_to_decimal('XC')
roman_to_decimal('LX')









