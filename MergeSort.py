# Function to implement merge sort
def mergeSort(array):  # Function name uses camel case
    # Base case: If the array has one or fewer elements, it's already sorted
    if len(array) <= 1:
        print(array)
        return array
    
    # Calculate the middle index to split the array into two halves
    midIndex = len(array) // 2
    
    # Divide the array into left and right halves
    leftHalf = array[:midIndex]  # Left half of the array
    rightHalf = array[midIndex:]  # Right half of the array
    
    # Recursively sort both halves
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)
    # Merge the two sorted halves into one sorted array
    m = merge(leftHalf, rightHalf)
    print(f'merge: {m}')
    print("hello")
    return m

# # Function to merge two sorted arrays into one sorted array
def merge(leftHalf, rightHalf):
    print(f"leftHalf2:{leftHalf}, rightHalf2:{rightHalf}")    
    mergedArray = []  # Initialize an empty list to hold the merged result

    # While both halves have elements, merge them based on the smaller value
    while leftHalf and rightHalf:
        if leftHalf[0] <= rightHalf[0]:
            mergedArray.append(leftHalf.pop(0))  # Add and remove the smallest from left
        else:
            mergedArray.append(rightHalf.pop(0))  # Add and remove the smallest from right
    print(f"before->mergedArray:{mergedArray}")
    # Append any remaining elements from either left or right
    mergedArray += leftHalf or rightHalf
    print(f"after->mergedArray:{mergedArray}")
    
    return mergedArray

# Test the mergeSort function with an example array
testArray = [12, 11, 13, 5, 6, 7, 10]  # Unsorted array
sortedArray = mergeSort(testArray)  # Apply merge sort
print("Sorted array:", sortedArray)  # Output the sorted array
