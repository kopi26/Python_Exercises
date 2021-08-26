#check ISBN Number

#print result
def to_print(result):
    if result:
        print('Valid ISBN Number')
    else:
        print('Invalid ISBN Number')

        
#ISBN number validation
def check_ISBN(num):
    num = list(num)
    #Remove sepiacl character
    char = ['-',' ']

    for x in num:
        if x in char:
            n = num.index(x)
            del num[n]    

    #check number count to define type
    count = len(num)
    tot = 0
    
    #For ISBN-13
    if (count==13):
        for i in range(count-1):
            if ((i+1) % 2) == 0:
                tot = tot + (int(num[i])*3)
            else:
                tot = tot + int(num[i])
                
        #get check digit             
        check_digit = (10-(tot%10))%10
        
        #check last digit
        if check_digit == int(num[count-1]):
            result = True
        else:
            result = False
            
    # For ISBN-10
    elif (count == 10):
        for i in range(9):
            tot = tot + int(num[i]) * (i+1)
                      
        #get check digit       
        check_digit = tot % 11

        #check last digit
        if (num[count-1] == 'X'):
            if(check_digit == 10):
                result = True
            else:
                result = False
        elif check_digit == int(num[count-1]):
            result = True
        else:
            result = False

    return to_print(result)
        
            


    
#Input ISBN Numbers
check_ISBN('978 04700 59029')
check_ISBN('0-321-14653-0')
check_ISBN('1-23456-789-X')
check_ISBN('0112112425')
