import math

#volume of Spherical Shell
def vol_shell(R,r):
    vol = 4/3*(math.pi*((R**3)-(r**3)))
    print('Volume of Spherical Shell is', round(vol,3))

vol_shell(3,3)
vol_shell(7,2)
