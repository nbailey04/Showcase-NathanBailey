list_length = 0                     # Initialize the variable "list_length" equal to 0 that will be edited later

class Node:                         # Create a Class called "Node"
    def __init__(self, data):       # Initializes any new objects of the class
        self.data = data            # Allows the call of .data to equal the data at that point
        self.next_node = None       # Leaves the next null value as 'None' because it does not exist (yet)

class LinkedList:                   # Create a class to manage the Linked List called "Linked List"
    def __init__(self):             # Initializes any new objects of the class
        self.head = None            # Since no data yet, we set the 'head' value as 'None'

    def append(self, data):         # Defines the 'append' method so that we can add "data"'s to the object
        global list_length          # This allows easy editing of the global variable 'list_length'
        list_length = list_length + 1 # This adds 1 to the variable 'list_length' every time you append a number so that it can have an accurate value of how many values are in the Linked List
        new_node = Node(data)       # Calls on the Node class to create a new 'Node' and stores it as new_node
        if not self.head:           # If a 'head' does not exists... (basically checks to see if there is a node already)
            self.head = new_node    # Make the 'head' value the new node (makes it the first node)
        else:                       # If there is already a 'head' value... (if there is already a node)
            current = self.head     # Set the current 'index' as the head of the Linked List
            while current.next_node:# This will run the loop for as long as there is a next node // it will stop at the last value
                current = current.next_node # This updates the 'current' variable as it goes through the Linked List
            current.next_node = new_node # Starts the new node at the end // meaning that the 'append' has been completed

    def remove(self, remove_number):# This defines the 'remove' method to remove things from the Linked List
        global list_length          # This allows easy editing of the global variable 'list_length'
        remove_position = (list_length - remove_number) + 1 # This makes a variable called 'remove_position' which is the exact position of number that you want to remove
        current = self.head         # This sets the current 'index' at te head of the Linked List
        previous = None             # Sets previous as 'None' because it is at the start and there is nothing before the start

        while current:              # Makes a loop that will run for as long as 'current' exists
            if 1 == remove_position:# Since we are bringing the remove position down by one every time the current moves up by one, when the remove_position = 1, the number that needs to be removed is found
                if previous:        # This checks to see if 'previous' exists
                    previous.next_node = current.next_node # If it does exist, then it sets the next node after the previous' 'index' as the same as the node after current's 'index'
                else:               # Runs this if there is no previous
                    self.head = current.next_node # Sets the new head of this iteration to the next node after the current
                return -1           # If everything else is false, then the number is found
            remove_position -= 1    # This brings the position value down for everytime that the current 'index' goes up
            previous = current      # Sets the new previous value as the current 'index'
            current = current.next_node # Moves the current 'index' to the next node

    def display(self):              # Defines a method to print the Linked List as '.display'
        current = self.head         # Sets the current 'index' as the head
        while current:              # Makes a loop that runs for as long as current exists
            print(current.data, end= " -> ") # Prints the value at the current 'index' and uses "end=" to keep it on the same line
            current = current.next_node # Moves the current index to the next node index
        print("None")               # After the print loop finishes, it adds "None" to end to signify that its at the end



"-----THIS IS WHERE THE ACTUAL CODE CALLS HAPPEN-----"
my_llist = LinkedList()             # This initializes a Linked List which is called 'my_llist'

my_llist.append(50)                 # This adds the number '58' to the linked list
my_llist.append(11)                 # This adds the number '11' to the linked list
my_llist.append(33)                 # This adds the number '33' to the linked list
my_llist.append(21)                 # This adds the number '21' to the linked list
my_llist.append(40)                 # This adds the number '40' to the linked list
my_llist.append(71)                 # This adds the number '71' to the linked list

my_llist.display()                  # This prints the Linked List after the numbers are added, adding the ' ->' after every number to show what node it is linked to

N = int(input("Which node from the end of the Linked List would you like removed? \n(the N-th node // N = _)?")) # This is an input code so that you can choose what index from the end that you want to delete and stored it as an integer to store
# ^^^^ you can just put the number of the index from the end you want to remove instead of the 'int(input("What number do you want gone?"))'
my_llist.remove(N)                  # This calls the method to remove the number that was inputted

my_llist.display()                  # This prints the Linked List after the number is removed, adding the ' ->' after every number to show what node it is linked to



"-----THE TEST CASES ARE BELOW AND LABELLED-----"

" What happens if you try to add a string"
# assert not isinstance(current.data, str), "The object you are trying to append is a string"
## This will have to go in the append method to make sure that the new node does not contain a string

" What happens if you input a letter when trying to remove"
# assert isinstance(N, int), "The number is not an integer"

" What happens if the number you tried to remove is not there"
# assert my_llist.remove(N) != -1, "The number you tried to remove does not exist in the Linked List"

" What happens if you want to remove from an empty list"
# assert list_length != 0, "Cannot remove from list, because the list is empty"
## This will have to go in the remove method to check if there are any nodes in the Linked List

" What happens if you choose a range outside of the list range"
# assert list_length >= remove_number, "You chose a position too large, the Linked List is not that large yet"
## This will have to go in the remove method to check if the linked list length has a bigger number of elements than indexes that the remove_number has from the end of the Linked List
