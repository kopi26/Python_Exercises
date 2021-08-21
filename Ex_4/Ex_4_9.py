import math

#calculate distance using Pythagorean theroem
def dist_calc(x1,y1,x2,y2):
   dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
   print('Distance between a and b is', round(dist,3))


dist_calc(x1=-2,y1=1,x2=4,y2=3)
dist_calc(x1=0,y1=0,x2=1,y2=1)

