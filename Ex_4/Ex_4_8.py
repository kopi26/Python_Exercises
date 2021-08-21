def sum_cube_calc(num):
    #check empty list
    if not num:
        return 0
    else:
        tot = 0
        for x in num:
            tot = tot + x**3
        return tot

print(sum_cube_calc([1,5,9]))
print(sum_cube_calc([3,4,5]))
print(sum_cube_calc([2]))
print(sum_cube_calc([]))
