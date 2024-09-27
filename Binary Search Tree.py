class TreeNode:                                             # Makes a class called 'TreeNode'
    def __init__(self, key):                                # Define the '__init__' function to initialize attributes whenever its called
        self.data = key                                     # Stores the key as 'self.data'
        self.left = None                                    # Sets the self.left attribute to None
        self.right = None                                   # Sets the self.right attribute to None

class BST:                                                  # Makes a class called 'BST'
    def __init__(self):                                     # Define the '__init__' function to inialize attributes whenever its called
        self.root = None                                    # Sets the self.root attribute to None
        self.lcount = 0                                     # Sets an attribute 'lcount' to keep track of the left node count
        self.rcount = 0                                     # Sets an attribute 'rcount' to keep track of the right node count

    def insert(self, data):                                 # Defines a function 'insert' used to insert values into the Binary Search Tree
        self.root = self._insert(self.root, data)           # Sets the root as whatever is returned from the '_insert' function

    def _insert(self, root, data):                          # Defines a function '_insert' used to do the hard work and recursive calls to return a new root value
        if root is None:                                    # This checks to see if the root does not equal 'None'
            return TreeNode(data)                           # If it does, then it will return the TreeNode Node initalized with the data given

        if data <= root.data:                               # This checks to see if the data used in the call is less than the root value
            root.left = self._insert(root.left, data)       # If it is, then it will store that as the left attribute of the current root
            self.lcount += 1                                # This updates the counter keeping track of the left nodes by adding 1
        else:
            root.right = self._insert(root.right, data)     # If not, it will store that as the right attribute of the current node
            self.rcount += 1                                # This updates the counter keeping track of the right nodes by adding 1

        return root                                         # At the end, it will return the root value to be stored in the self.root in the 'insert' function

    def delete_root(self):                                  # Define a function to delete the root node
        if self.root is None:                               # This checks to see if the self.root attribute equals 'None'
            return                                          # If it does, then we know it is empty and do not need to continue through and can just return

        if self.root.left is None:                          # This checks to see if the '.left' attribute of the root is 'None'
            self.root = self.root.right                     # If it is, then it will set the root as the right root attribute because thats the only one left
            self.rcount -= 1                                # It will then update the counter by subtracting 1 since we just got rid of one
        elif self.root.right is None:                       # This checks to see if the '.right' attribute of the root is 'None'
            self.root = self.root.left                      # If it is, then it will set the root as the left root attribute because thats the only one left
            self.lcount -= 1                                # It will then update the counter by subtracting 1 since we just got rid of one
        else:
            # Find the maximum value in the left subtree
            max_left = self.find_max(self.root.left)        # If right and left exist, then it will store the max value in the left subtree
            self.root.data = max_left.data                  # Sets the root data as the max value in the left subtree, deleting the root
            self.root.left = self.delete_max(self.root.left)# Sets the .root.left attribute as what is returned from the 'delete_max' function

    def find_max(self, node):                               # Defines a function called 'find_max' that uses a variable 'node'
        while node.right:                                   # This runs for as long as the '.right' attribte exists of the 'node'
            node = node.right                               # It sets node as the right for as long as there is one because the right-most value will be the max
        return node                                         # This returns the node

    def delete_max(self, node):                             # Defines a function called 'delete_max' intended to delete the max
        if node.right is None:                              # This checks to see if the '.right' attribute exists
            return node.left                                # If it does then it will return the node.left
        node.right = self.delete_max(node.right)            # This sets the .right attribute of the node as the value returned from the recursive call of the 'delete_max' function
        return node                                         # This returns the node

    def display(self):                                      # Defines a function called 'display()'
        self.tree = []                                      # Creates a list meant to track the length of numbers in the tree
        print(self._display(self.root))                     # This prints the value returned from the '_display' function


        if self.lcount > self.rcount:                       # This checks to see if the left node count is larger than the right node count
            return 'LS'                                     # If it is, then it will return "LS"
        elif self.lcount < self.rcount:                     # This checks to see if the left node count is less than the right node count
            return 'RS'                                     # If it is, then it will return "RS"
        return self._display(self.root)                     # Otherwise, it will return whatever is returned from the '_display' function


    def _display(self, root):                               # Defines a function called '_display' to do all the hard work meant
        if root is not None:                                # This checks to see that the root is not 'None'
            self._display(root.left)                        # If it is not 'None' then it will perform recursive calls starting at the left-most "leaf/node"
            #print(root.data, end= " ")                     # This will print the Binary Search Tree
            self.tree.append(root.data)                     # This adds all the values that it comes across so that it is easier to validate
            self._display(root.right)                       # This will then go to the left-most value of the right subtree and then recursive call until the right-most value
        else:
            return None                                     # Otherwise it will return 'None'
        if len(self.tree) == 2:                             # This checks the tracking list made earlier to make sure that the list is long (goes hand in hand with the second assert statement
            return 1                                        # If it is not, then it will return 1 (to be asserted by the second assert statemnt
        return True                                         # Otherwise it will return 'True'

# Driver code
bst = BST()                                                 # Initializes BST() as bst
bst.insert(4)                                               # This adds 4 to the tree
bst.insert(2)                                               # This adds 2 to the tree
bst.insert(6)                                               # This adds 6 to the tree
bst.insert(1)                                               # This adds 1 to the tree
bst.insert(3)                                               # This adds 3 to the tree
bst.insert(5)                                               # This adds 5 to the tree
bst.insert(7)                                               # This adds 7 to the tree

print("Original BST:")
bst.display()


bst.delete_root()                                           # Deletes the root and replaces it with the appropriate value

print("\nBST after deleting the root:")
bst.display()

"TEST CASES BELOW"
'What happens in the is no numbers in the BST'
#assert bst.display() != None , 'There are no values in the Binary Search Tree'

'What happens if there are only 2 branching elements in the BST from the root'
#assert bst.display() != 1, 'There are only 2 branching elements from the root'

'What happens if the tree is right skewed and not height-balanced'
#assert bst.display() != 'RS', 'The tree is right skewed and not height-balanced'

'What happens if the tree is left skewed and not height-balanced'
#assert bst.display() != 'LS', 'The tree is left skewed and not height-balanced'
