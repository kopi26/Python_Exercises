'''
1. Leap or common year

Write a function that returns true or false depending on whether its input integer
is a leap year or not.

A leap year is defined as one that is divisible by 4, but is not otherwise
divisible by 100 unless it is also divisible by 400.

For example, 2001 is a typical common year and 1996 is a typical leap year,
whereas 1900 is an atypical common year and 2000 is an atypical leap year.

'''

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
    return result
        
#Years to be checked

years = [2001, 1996, 1900, 2000]

for year in years:
    print(f"{year} ", end = '')
    if find_leap(year):
        print("is a leap year")
    else:
        print("is a common year")
