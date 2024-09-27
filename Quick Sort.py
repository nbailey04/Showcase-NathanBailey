arr = [50, 11, 33, 21, 40, 50, 40, 21, 40] #expected output of [11, 21, 33, 40, 50]
farr = [] #initializes a new array that will serve as the filtered array

for i in range(len(arr)): #this sets up the distance/length that the for loop will run for
    if arr[i] not in farr: #this checks if the current value is already in the second, filtered array (farr)
        farr.append(arr[i]) #if the value is not already in the filtered array (farr), then it will add the new value to the array
#at this point, the filtered array is shown below
#[50, 11, 33, 21, 40]
#this array is not sorted and will need to be sorted without using any library functions

def quick_sort(arr): #we define the function "quick_sort(arr)" so that we can call this function later
    if len(arr) <= 1: #this checks to see if the array is long enough to use the quick_sort() function on
        return arr #if it is not long enough, it just returns the array because its already "sorted" (not really but its not long enough to be coonsidered as "unsorted")

    pivot = arr[len(arr) // 2]  #places a "pivot" located in roughly the center of the array
    larr = [x for x in arr if x < pivot] #this checks every iteration of the array (farr) and checks to see if it is less than the pivot value // if it is, then add it to a new array know as "larr"
    marr = [x for x in arr if x == pivot] #this checks every iteration of the array (farr) and checks to see if it is equal to the pivot value // if it is, then add it to a new array know as "marr"
    harr = [x for x in arr if x > pivot] #this checks every iteration of the array (farr) and checks to see if it is less than the pivot value // if it is, then add it to a new array know as "harr"

    return quick_sort(larr) + marr + quick_sort(harr) #this does a recursive call to "Quick Sort" the previously separated arrays (larr and harr)
#I do this so i can have a way so that it will run not a certain amount of time, but a time dependant on the number of elements in the sorted array (farr)
#[11, 21, 33, 40, 50]

print(quick_sort(farr)) #this calls the function "quick_sort()" and places the array 'farr' in the place of the array that will be sorted
#it then prints the array

"-----------TEST CASES BELOW-----------"
#One would be to test the array and see if there is any elements in it:
# assert bool(arr), "There are no elements in the array."

#Another way you could check to see if there are any strings in the array:
# assert not(any(isinstance(item, str) for item in arr)), "You have a string in your array."

#A third way could be to test if there are any non-numbers at all in the array:
# assert not(any(not isinstance(item, (int, float)) for item in arr)), "There is a non-number element that exist in your array"
