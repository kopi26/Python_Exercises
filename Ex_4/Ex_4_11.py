import math

#calculate area of Hexagon
def hexa_area(length):
    area = (3*math.sqrt(3)*(length**2))/2
    print('Area of Hexagon is', round(area,1))

hexa_area(1)
