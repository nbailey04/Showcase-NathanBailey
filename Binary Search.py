arr = [3, 4, 5, 6, 7, 0, 1, 2]
arr.sort()

print(arr)
x = int(input("Select a number"))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Check if the target is equal to the middle element
        if arr[mid] == target:
            return mid
        # If the target is smaller, search the left half
        elif arr[mid] > target:
            right = mid - 1
        # If the target is larger, search the right half
        else:
            left = mid + 1
    # If the target is not found in the array, return -1
    return -1
result = binary_search(arr, x)
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print(f"Element {x} not found in the array")
