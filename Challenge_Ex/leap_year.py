#find leap or common year
def find_leap(year):
    if (year % 100) == 0:
        if (year % 400) == 0:
            result = True
        else:
            result = False
    elif (year % 4) == 0:
        result = True
    else:
        result = False
        
    #function call to print result   
    print_result(result)


#check result
def print_result(result):
    if result:
        print('Leap year')
    else:
        print('Common year')


#Years to be checked
find_leap(2001)
find_leap(1996)
find_leap(1900)
find_leap(2000)
