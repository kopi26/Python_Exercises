import math

#calculate height of Equilateral Triangle
def equal_tri(side):
    height = (side*math.sqrt(3)/2)*10
    print('Height of Equilateral Triangle is', round(height,2) ,'mm')

equal_tri(2)
equal_tri(5)
