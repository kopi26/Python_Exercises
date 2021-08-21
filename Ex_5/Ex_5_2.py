#read random line

import random
line = open('doc1.txt','r').read().splitlines()#split each lines
random_line = random.choice(line)
print(random_line)

