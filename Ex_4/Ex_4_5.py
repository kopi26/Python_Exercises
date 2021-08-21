def area_calc(base,height,shape):
    if shape == 'triangle':
        print('Area of Triangle is', (base*height)/2)
    elif shape == 'parallelogram':
        print('Area of parallelogram is', base*height)
    else:
        print('Invalid Shape!')

area_calc(2,3,'triangle')
area_calc(8,6,'parallelogram')
