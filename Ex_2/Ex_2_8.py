#calculate area and perimeter of rectangle using user inputs

#Read length and height as user inputs
length = float(input('Enter the length: '))
height = float(input('Enter the height: '))

#calculate the area
area = length * height

#calculate the perimeter
peri = 2*(length + height)

print('Area of Rectangle is: ', area , '\nPerimeter of Rectangle is: ', peri)
