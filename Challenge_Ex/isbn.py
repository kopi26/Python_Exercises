#check ISBN Number

#ISBN number validation
def check_isbn(isbn_code):
    #Remove sepiacl character
    isbn_code = isbn_code.replace('-', '')
    isbn_code = isbn_code.replace(' ', '')

    #check number count to define type
    count = len(isbn_code)
    tot = 0
    
    #For ISBN-13
    if (count==13):
        for i in range(count-1):
            if (i % 2) == 0:
                tot = tot + int(isbn_code[i])
            else:
                tot = tot + (int(isbn_code[i])*3)
                
        #get check digit             
        check_digit = (10-(tot%10))%10
        
        #check last digit
        if check_digit == int(isbn_code[-1]):
            result = True
        else:
            result = False
            
    # For ISBN-10
    elif (count == 10):
        for i in range(count-1):
            tot = tot + int(isbn_code[i]) * (i+1)
                      
        #get check digit       
        check_digit = tot % 11

        #check last digit
        if (isbn_code[count-1] == 'X'):
            if(check_digit == 10):
                result = True
            else:
                result = False
        elif check_digit == int(isbn_code[-1]):
            result = True
        else:
            result = False
    #Invalid ISBN
    else:
            result = False

    return result
        
            
#Input ISBN Numbers
isbn_codes = [ '978 04700 59029',
               '0-321-14653-0',
               '1-23456-789-X',
               '0112112425' ]

for isbn in isbn_codes:
    print(f"{isbn:16} is ", end = '')
    if check_isbn(isbn):
        print("Valid")
    else:
        print("Invalid")
