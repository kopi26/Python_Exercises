#count repitition frequency of word

#empty dictionary
rep_word = dict()

#read file
with open('rep_text.txt','r') as f:
    for line in f:
        line = line.lower().split()
        
        for x in line:
            if x in rep_word:
                rep_word[x] += 1
            else:
                rep_word[x] = 1

    f.close()

#print frequency count
for x in rep_word.keys():
    print(x, ':', rep_word[x])
