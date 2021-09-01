#Combined a large number from list of numbers

from itertools import permutations

def combine_large(num):
    perm = permutations(num)
    large_num = 0

    for x in perm:
        num_list = map(str,x)
        num = ''.join(list(num_list))
        if int(num) > large_num:
            large_num = int(num)

    print(large_num)
 
    

combine_large([35, 5, 10, 9]) # 9+5+35+10
combine_large([50, 2, 1, 9])    #95021
combine_large([5, 50, 56])      #56550     
combine_large([420, 42, 423])   #42423420
