##1
def tri_area(base,height):
    return (base*height)/2

area = tri_area(3,2)
print('Area of Triangle is', area)



##2
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



##3
#finds the maximum range of a triangle's third edge
def max_range(side1, side2):
    return (side1+side2)-1

max_side = max_range(8,10)
print("Maximum range of Triangle's third edge", max_side)



##4
def peri_rec(length,width):
    return 2*(length+width)

peri = peri_rec(6,7)
print('Perimeter of Rectangle is', peri)



##5
def area_calc(base,height,shape):
    if shape == 'triangle':
        print('Area of Triangle is', (base*height)/2)
    elif shape == 'parallelogram':
        print('Area of parallelogram is', base*height)
    else:
        print('Invalid Shape!')

area_calc(2,3,'triangle')
area_calc(8,6,'parallelogram')



##6
def n_side(num):
    switcher = {
        1 : "circle",
        2 : "semi-circle",
        3 : "triangle",
        4 : "square",
        5 : "pentagon",
        6 : "hexagon",
        7 : "heptagon",
        8 : "octagon",
        9 : "nonagon",
        10: "decagon"
        }
    return switcher.get(num,'not exist!')

num  = int(input('Enter a number: '))

#check whole number
if num > 0:
    shape = n_side(num)
    print('Shape is', shape)
else:
    print('Invalid number!')



##7
import math

#calculate height of Equilateral Triangle
def equal_tri(side):
    height = (side*math.sqrt(3)/2)*10
    print('Height of Equilateral Triangle is', round(height,2) ,'mm')

equal_tri(2)
equal_tri(5)



##8
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



##9
import math

#calculate distance using Pythagorean theroem
def dist_calc(x1,y1,x2,y2):
   dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
   print('Distance between a and b is', round(dist,3))


dist_calc(x1=-2,y1=1,x2=4,y2=3)
dist_calc(x1=0,y1=0,x2=1,y2=1)



##10
import math

#calculate vloume of cone
def cone_volume(h,r):
    if(r>0 and h>0):
        volume = (math.pi*(r**2)*h)/3 
        return round(volume,2)
    else:
        return 0
    
print(cone_volume(3,2))
print(cone_volume(15,6))
print(cone_volume(18,0))


##11
import math

#calculate area of Hexagon
def hexa_area(length):
    area = (3*math.sqrt(3)*(length**2))/2
    print('Area of Hexagon is', round(area,1))

hexa_area(1)



##12
#volume of box
def box_vol(width,length,height):
    vol = length*width*height
    print('Volume of box is', vol)

box_vol(2,5,1)



##13
import math

#volume of Spherical Shell
def vol_shell(R,r):
    vol = 4/3*(math.pi*((R**3)-(r**3)))
    print('Volume of Spherical Shell is', round(vol,3))

vol_shell(3,3)
vol_shell(7,2)



##14
import math

#Calculate length of the cube's main diagonal from volume
def cube_diagonal(vol):
    length = vol**(1/3)
    diagonal = length * math.sqrt(3)
    return round(diagonal,2)

print(cube_diagonal(8))
print(cube_diagonal(343))



##15
import math

#find triangle length
def length_tri(point1,point2):
   length = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)
   return length

#find perimeter
def peri_tri(cor):        
    l1 = length_tri(cor[0],cor[1])
    l2 = length_tri(cor[1],cor[2])
    l3 = length_tri(cor[0],cor[2])
    peri = l1+l2+l3
    return round(peri,2)

print(peri_tri([[15, 7], [5, 22], [11, 1]]))
print(peri_tri([ [0, 0], [0, 1], [1, 0] ]))





