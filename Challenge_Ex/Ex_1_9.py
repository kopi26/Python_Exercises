#Find Greatest common diviser

#Input numbers
a,b = 18,48

#method 1
import math
print(math.gcd(a,b))


#method 2
def gcd(a,b):
    if(a==0):
       return b
    if(b==0):
        return a
    
    #Euclidean algorithm 
    return gcd(b,(a%b))



print(gcd(a,b))



        
