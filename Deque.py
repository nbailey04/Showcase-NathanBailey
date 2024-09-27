from collections import deque                   # This imports deque from collections
class Queue:                                    # Defines a class called 'Queue'
    def __init__(self):                         # This defines a initialization 'sequence' that creates a list when called
        self.len = -1                           # This defines a variable that will keep track of the length of the Main Queue
        self.lent = -1                          # This defines a variable that will keep track of the length of the Max Queue
        self.main = deque()                     # This sets an empty queue as self.main
        self.max = deque()                      # This sets an empty queue as self.max

    def add(self, item):                        # Defines a function 'add(item)' that will be used to add items to the queue
        # assert item != None, "The number you tried to add was 'NoneType'"    # This is a test case (Test case #1) to make sure that you do not add 'None' to the queue
        self.main.append(int(item))             # This adds the number as an 'int' to the Main Queue
        self.max.append(int(item))              # This adds the number as an 'int' to the Max Queue
        self.len += 1                           # This adds 1 to the variable 'self.len' that keeps track of the Main Queue length
        self.lent += 1                          # This adds 1 to the variable 'self.lent' that keeps track of the Max Queue length
        if self.len > 0:                        # This checks to see if length of the Main Queue is greater than 0
            a = self.max.pop()                  # If it is, then it will 'pop' the most recent value of the Max Queue and store it as 'a'
            b = self.max.pop()                  # and then store the next value that is 'pop'-ed as 'b'
            self.lent -= 2                      # This accounts for the decrease in the length of the Max Queue from the previous 'pop's
            if a > b:                           # This checks to see if the value of a is greater than b
                self.max.append(a)              # If it is, then it will add the larger value, 'a', to the Max Queue
                self.lent += 1                  # The previous step increased the length by 1, so this is to account for the change

            # This whole elif block ensure that 2 numbers are not added to the Maximum Queue consecutively
            #elif a == b:
            #    self.max.append(a)
            #    self.lent += 1


            else:                               # Otherwise...
                self.max.append(b)              # This will re-add the 'pop'-ed values to the Max Queue starting with 'b'
                self.max.append(a)              # Then it will add the value of 'a' back to the Max Queue as well
                self.lent += 2                  # This is to account for the change in length that occurred to the Max Queue in the previous step

    def display(self):
        #assert self.len != -1, 'There is nothing in the queue // The queue is empty'       # This is a test case (Test Case #2) that makes sure that the queue is not empty before displaying the queue
        #assert self.len != 0, 'There is only 1 item in the queue'                          # This is a test case (Test Case #3) that makes sure that the queue does not only have 1 element in it before displaying the queue

        count = self.len                                            # This stores the length of the Main Queue as 'count' so that it can be edited without affecting the actual length // it will serve as an index number
        print("Main Queue", end= ': ')                              # This prints "Main Queue: " an keeps it on the same line so that the Main Queue elements can come after in the following while statement
        while count != 0:                                           # This will run the following code for as long as count does not equal 0
            print(self.main[count], end= '->')                      # This will print every element of the queue followed by an arrow on the same line until the first value
            count -= 1                                              # This subtracts one from the index number so that it can display the correct number
        print(self.main[count], " << front of Queue")               # This prints the first value of the Main Queue with a arrow at the front to further demonstrate the location of the front of the queue

        count = self.lent                                           # This stores the length of the Max Queue as 'count' so that it can be edited without affecting the actual length // it will serve as an index number
        print("Max Queue", end=': ')                                # This prints "Max Queue: " an keeps it on the same line so that the Max Queue elements can come after in the following while statement
        while count != 0:                                           # This will run the following code for as long as count does not equal 0
            print(self.max[count], end='->')                        # This will print every element of the queue followed by an arrow on the same line until the first value
            count -= 1                                              # This subtracts one from the index number so that it can display the correct number
        print(self.max[count], ' << front of Queue')                # This prints the first value of the Max Queue with a arrow at the front to further demonstrate the location of the front of the queue

    def max_number(self):                                           # This will find the front of the Max Queue and display the max number in the Main Queue
        print(f"The max number in the queue is -> {self.max[0]}.")

"-----BELOW ARE THE DRIVER CODES-----"
ML = Queue()                # Initializes ML in the 'Queue()' class
ML.add(1)                   # Adds 1 to the queue
ML.add(4)                   # Adds 4 to the queue
ML.add(2)                   # Adds 2 to the queue
ML.add(4)                   # Adds 4 to the queue
ML.display()                # This will display the queue in the same format as on the lab sheet
ML.max_number()             # This will display the max number (aka the first element in the queue)



"-----TEST CASES-----"

'What happens if there is a queue with "None" in it'
#assert item != None, "The number you tried to add was 'NoneType'"
#This is best used in Line 10

'What happens if there is a queue with nothing in it'
#assert self.len != -1, 'There is nothing in the queue // The queue is empty'
#This is best used in Line 35

'What happens if there is only one element in the queue'
#assert self.len != 0, 'There is only 1 item in the queue'
#This is best used in Line 36

'What happens if you wanted to make sure you cannot add duplicate elements to the Maximum Queue consecutively'
# REFER TO LINE 23



'----------BELOW IS A USE FOR DEQUE-----------'


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


