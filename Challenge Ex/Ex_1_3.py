#find all permutations of a string

#swap letters of string
#string, start index, end index as arguements
def swap(word,start,end):
    if (start==end):
        print(join_word(word))
    else:
        for i in range(start,(end+1)):
            #swap letters
            word[start], word[i] = word[i], word[start]
            #Recursion to swap letters 
            swap(word,(start+1),end)
            #change to back format
            word[start], word[i] = word[i], word[start]
    


#join letters
def join_word(letters):
    return ''.join(letters)

#permutation word
string1 = 'ABC'
swap(list(string1),0,len(string1)-1)
print()
string2 = 'biro'
swap(list(string2),0,len(string2)-1)
