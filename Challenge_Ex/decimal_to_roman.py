#Covert Decimal to Roman

def decimal_to_roman(num):
    values = {
        1   :   'I',
        4   :   'IV',
        5   :   'V',
        9   :   'IX',
        10  :   'X',
        40  :   'XV',
        50  :   'L',
        90  :   'XC',
        100 :   'C',
        400 :   'CD',
        500 :   'D',
        900 :   'CM',
        1000:   'M'
        }

    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ''
    num  = int(num)

    for x in num_list:
        quotient = num // x

        #roman is equal to quotient multiplication
        if (quotient > 0):
            roman += values[x] * quotient

        #update the integer value
        num = num % x

    #print decimal value
    print(roman)


decimal_to_roman(357)
            

