#Find square root

def Babylonion_square_root(num):
    x = num
    y = 1 #initiate approximate root as 1

    error = 0.00001 # accuracy level

    while(x-y) > error:
        x = (x+y)/2
        y = num/x
    return x


#Inupt numbers
print(round(Babylonion_square_root(9),2))
print(round(Babylonion_square_root(3),2))
