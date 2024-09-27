array_1 =[1, 6, 9, 10, 11, 21]     # This is where you would want to define the arrays that will be search
array_2 = [2, 6, 9, 11, 17, 21]    # ^^^same thing as stated above
f_array1 = []                      # This is the final array that is to be printed, initialized (will be used in the corresponding number's test)
f_array2 = []                      # This is the final array that is to be printed, initialized (will be used in the corresponding number's test)
f_array3 = []                      # This is the final array that is to be printed, initialized (will be used in the corresponding number's test)

# The expected output after each 'test' code runs should be [6, 9, 11, 21]

'''
EVERY LARGE BREAK IN THE CODE IS THE END OF THE THAT TEST CODE

AFTER EVERY TEST SEGMENT, YOU WILL FIND THE TEST CASES
'''




"-------THIS IS THE START OF THE FIRST TEST-------"
def test_1(x, y):                       # This is the first test to run with an O(m * n) run time notation

    for i in range(len(x)):             # For every element in the range of the length of x (in this case x = array_1)

        for j in range(len(y)):         # For every element in the range of the length of y (in this case y = array_2)

            if x[i] == y[j]:            # To test if the 2 values are equivalent

                f_array1.append(y[j])   # This adds from the second array (array_2) to the final array (f_array)if this number is also found in the first array (array_1)

    print(f"Test 1: {f_array1}")        # This prints an f-string so that it out puts the computed final array (f_array)

test_1(array_1, array_2)                # The linear "Brute Force" search

'''
Test cases:
'''
# What happens if there is no array for one of the arrays:
# assert bool(array_1) and bool(array_2), "One or both of the arrays are empty"

# What happens if they are different lengths:
# assert len(array_1) == len(array), "They are different lengths"

# What happens if there is only one number in one of the arrays:
# assert len(array_1) > 1 and len(array_2), "There is only 1 number in one or both arrays

# What happens if there is a word/string in the array:
# assert not(any(isinstance(item, str) for item in array_1 or array_2)), "You have a string in your array."





"-------THIS IS THE START OF THE SECOND TEST-------"
def binary_search(arr, target):
    left = 0                                # Initialize a left bound

    right = len(arr) - 1                    # Initializes a right bound

    while left <= right:                    # This has it loop until the bounds meet (meaning the number is not in the list)

        mid = left + (right - left) // 2    # Establishes a "middle" point of the array to be searched

        if arr[mid] == target:              # This checks if the target is equal to the middle element

            return mid                      # If the target equals the mid value of the array, return the position

        elif arr[mid] > target:             # Checks if the target is greater than the mid value of the array

            right = mid - 1                 # If the target is less than the mid value of the array, alter the higher bound to be 1 lower than the middle and estabish a new higher bound
        else:
            left = mid + 1                  # If the target is not greater than or equal to the mid value of the array, alter the lowerbound to be 1 higher than the mid

    return -1                               # Returns -1 if the value is not found in the array

def test_2(x, y):                                   # This defines the fuction of the Second Test (O(mlog(n))/O(nlog(m)) time)
            #In this case x = array_1 and y = array_2
    for i in x:                                     # For every item in the given array: x (in this case x = array_1)

        test2r = binary_search(y, i)                # Makes a call to the previously defined function "binary_search(arr, target)" where in this case, arr = y and the target = current index value of x (aka array_1) and then stores the returned value as "test2r"

        if test2r not in f_array2 and test2r != -1: # This checks to see if the returned value "test2r" is already in the final array (in this case f_array2) and that the returned value "test2r" does not equal -1 (which means its not found)

            f_array2.append(y[test2r])              # If the returned value "test2r" passes the tests previously stated, then it adds the value in the array "y" (aka array_2) at the position given by "test2r"

    print(f"Test 2: {f_array2}")                    # Prints the f-string with the newly edited array (f_array2)

test_2(array_1, array_2) #the binary "O(mlog(n))/O(nlog(m))" search

'''
Test cases:
'''
# What happens if there is no array for one of the arrays:
# assert bool(array_1) and bool(array_2), "One or both of the arrays are empty"

# What happens if they are different lengths:
# assert len(array_1) == len(array), "They are different lengths"

# What happens if there is only one number in one of the arrays:
# assert len(array_1) > 1 and len(array_2), "There is only 1 number in one or both arrays

# What happens if there is a word/string in the array:
# assert not(any(isinstance(item, str) for item in array_1 or array_2)), "You have a string in your array."





"-------THIS IS THE START OF THE THIRD TEST-------"
def test_3(x, y):                   # This defines the fuction of the Third Test (O(N) time)
            #In this case x will be array_1 and y will be array_2
    for i in x and y:               # For every element in the given array: x(in this case x = array_1)

        if i in x and y:            # This checks to see if the index in x(x = array_1) at position i is in the other array (y = array_2)

            f_array3.append(i)      # If the value is in y (in this case y = array_2)then it will add it to the final array (f_array3)

    print(f"Test 3: {f_array3}")    # Prints the f-string with the newly edited array (f_array3)

test_3(array_1, array_2) #the linear run of O(m + N) or O(N)

'''
Test cases:
'''
# What happens if there is no array for one of the arrays:
# assert bool(array_1) and bool(array_2), "One or both of the arrays are empty"

# What happens if they are different lengths:
# assert len(array_1) == len(array), "They are different lengths"

# What happens if there is only one number in one of the arrays:
# assert len(array_1) > 1 and len(array_2), "There is only 1 number in one or both arrays

# What happens if there is a word/string in the array:
# assert not(any(isinstance(item, str) for item in array_1 or array_2)), "You have a string in your array."
