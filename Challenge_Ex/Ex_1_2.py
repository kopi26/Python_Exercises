#check balance parantheses

#open parantheses
open_paran = ['(', '{', '[']
close_paran = [')','}', ']']

def check_balance(string):
    stack = []
    #check empty list
    if not string:
        print('Empty string')
    else:
        for x in string:
            #open braces added to stack
            if x in open_paran:
                stack.append(x)
            #close braces checked with last element of stack then pop out from stack
            elif x in close_paran:
                index = close_paran.index(x)
                if(len(stack)>0 and (open_paran[index] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    break
            else:
                print('Invalid character is exist')
                
        #balance stack should be an empty list
        if (len(stack) == 0):
            print('balanced')
        else:
            print('unbalanced')


#Input strings
check_balance('{{)(}}')     #not balance
check_balance('({)}')       #not balance
check_balance('[({})]')     #balance  
check_balance('{}([])')     #balance
check_balance('{()}[[{}]]') #balance
            
