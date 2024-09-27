from collections import deque                           # This imports 'deque' from 'collections'

def Evaluation(exp):                                     # Defines a function
    stack = deque()                                      # Initializes 'stack' as an empty stack
    elements = exp.split()                               # This splits the expression at every space
    op_num = 0                                           # This is going to keep track of the amount of operators

    for i in elements:                                   # For every element in the stack "elements"
        if i.isdigit():                                  # Checks to see if the current element is an integer
            stack.append(int(i))                         # If it is, then it will add the number to the stack
        elif (i == '+' or i == '-') and len(stack) == 0: # This checks to see if the current index is a operator or not and if the stack is empty
            return "1 operator"                          # If it is, it returns that there is only 1 operator in the stack
        elif (i == '+' or i == '-') and len(stack) == 1: # This checks to see if the current index is an operator or not, and if the stack has only one number besides the operator
            return "1 number with 1 operator"            # If it is true, then it will returm the phrase '1 number with 1 operator'
        else:                                            # If everything else did not check
            a = stack.pop()                              # This stores the first element 'pop'ed
            b = stack.pop()                              # This stores the second element 'pop'ed
            if i == '+':                                 # This checks to see if the 'i' is equal to '+'
                result = a + b                           # This stores the result of the sum of a and b
                op_num += 1                              # This adds 1 to the op_num variable so that we can keep track of the operators detected
            elif i == '-':                               # This checks to see if the element 'i' is equal to '-'
                result = b - a                           # This stores the result of the difference between b and a
                op_num += 1                              # This adds 1 to the op_num variable so that we can keep track of the operators detected
            else:                                        # If all the other if statements were false then...
                raise ValueError("Invalid Operator")

            stack.append(result)                         # This adds whatever the result is based off the previous cases to the stack
    if len(stack) == 0:                                  # This tests to see if the stack is empty
        return 'empty'                                   # If it is empty, then it will return the phrase 'empty'
    if len(stack) == 1 and op_num == 0:                  # This checks the length of the stack and the numbers of operators used
        return 'one'                                     # If it is equal to 1, then it will return the phrase 'one'
    return stack.pop()                                   # The previous if statements were to return phrases for the test cases // this one is if they all come back as false, then it will return the value of evaluated expression


"THIS IS WHERE THE CODE RUNS"

exp = "3 5 + 1 -" #     -----THIS IS WHERE YOU WOULD INPUT THE POST-FIX EXPRESSION-----
print(Evaluation(exp))  # This is where it calls back on the Evaluation function and takes the prevoulsy defined variable 'exp'

"-----TEST CASES-----"

'What happens if there is the stack is empty / ex: " "'
#assert Evaluation(exp) != 'empty', "Its empty"

'WHat happens if there is only one integer / ex: "1"'
#assert Evaluation(exp) != 'one', "There is only one integer in this 'expression'"

'What happens if there is only one operator / ex: "+"'
#assert Evaluation(exp) != '1 operator', "There is only one operator in the stack"

'What happens if the expression is a number and an operator / ex: "2 +"'
#assert Evaluation(exp) != '1 number with 1 operator', "There is only a number followed by a operator"


