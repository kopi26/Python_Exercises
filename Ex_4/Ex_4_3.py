#finds the maximum range of a triangle's third edge
def max_range(side1, side2):
    return (side1+side2)-1

max_side = max_range(8,10)
print("Maximum range of Triangle's third edge", max_side)
