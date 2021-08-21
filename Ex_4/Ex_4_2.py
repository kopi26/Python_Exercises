def rec_area(length,width):
    if(length > 0 and width > 0): 
        return length*width
    else:
        return -1

area = rec_area(3,4)

if area == -1:
    print('Invalid arguments!')
else:
    print('Area of Rectangle is', area)
