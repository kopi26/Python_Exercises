#Combined as large number

def combine_large(num):
    num_list = []
               
    #convert to string
    str_num = [str(x) for x in num]
    print(str_num)

    for x in str_num:
        for y in x:
            
            
    #return print(''.join(str_num))


#check non-negative numbers
def check_num(num_list):
    for x in num_list:
        if x < 0:
            print('Negative number is exist')
            break
    combine_large(num_list)

combine_large([35, 5, 10, 9]) # 9+5+35+10
#combine_large([50, 2, 1, 9])    #95021
#check_num([5, 50, 56])      #56550     
#check_num([420, 42, 423])   #42423420
