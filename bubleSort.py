# Bubble Sort 
""" 
* the simplest sorting algorithm
* repeatedly swapping the adjacent elements if they are in the wrong order.
* not suitable for large data sets as its average and worst case time complexity is quite high.

"""


def bubbleSort(arr): 
    n = len(arr)

    for i in range(n): # Control range to run
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 7, 1, 10]

bubbleSort(arr)

print(arr)

"""
        [5, 7, 1, 10]
index    0  1  2   3   => n=  4

        i = 0; j -> [0, 3)
        [5, 7, 1, 10, 8, 9, 2] => i = 0;    j=0,    a[j] = 5;   a[j+1] = 7;     5 > 7
        [5, 1, 7, 10, 8, 9, 2] => i = 0;    j=1,    a[j] = 7;   a[j+1] = 1;     7 > 1
        [5, 1, 7, 10, 8, 9, 2] => i = 0;    j=2,    a[j] = 7;   a[j+1] = 1;     7 > 1


"""