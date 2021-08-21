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


