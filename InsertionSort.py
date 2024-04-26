def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        print(f"key: {key}")
        j = i-1
        print(f"arr_before: {arr}")
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            print(f"arr[j+1]: {arr[j+1]}, arr[j]:{arr[j]}")
            arr[j+1] = arr[j]  # Shift elements to the right
            print(f"arr_change: {arr}")
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
        print(f"arr:{arr}")
  
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [6,1,7,4,2,9,8,5,3]
insertionSort(arr)
print(arr)
