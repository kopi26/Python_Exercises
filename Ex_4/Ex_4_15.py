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





