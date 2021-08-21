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
    
