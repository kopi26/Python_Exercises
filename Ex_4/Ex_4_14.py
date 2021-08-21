import math

#Calculate length of the cube's main diagonal from volume
def cube_diagonal(vol):
    length = vol**(1/3)
    diagonal = length * math.sqrt(3)
    return round(diagonal,2)

print(cube_diagonal(8))
print(cube_diagonal(343))
