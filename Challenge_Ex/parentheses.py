#check balance parantheses

#open parantheses
open_paran = ['(', '{', '[']
close_paran = [')','}', ']']

def check_balance(string):
    stack = []
    for x in string:
        #open braces added to stack
        if x in open_paran:
            stack.append(x)
        #close braces checked with last element of stack then pop out from stack
        elif x in close_paran:
            index = close_paran.index(x)
            if(len(stack)>0 and (open_paran[index] == stack[-1])):
                stack.pop()
            else:
                break
    #balance stack should be an empty list
    if stack:
        return False
    else:
        return True


#Input strings
strings = ['{{)(}}',    #unbalanced
 '({a)}',                #unbalanced
 '[a({})]',              #balanced
 '{}([]a)',              #balanced
 '{(a)}[[{}]]']          #balanced

for string in strings:
    print(f" {string:12}", end = '')
    if check_balance(string):
        print(" balanced")
    else:
        print(" unbalanced")
