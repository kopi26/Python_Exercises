#find logest word

#read file
with open('test.txt', 'r') as f:
    word = f.read().split()
    max_length = 0
    for x in word:
        if len(x) > max_length:
            max_length = len(x)
            long_word = x
    f.close()

#print longest word
print(f'Longest word of file: {long_word}')
