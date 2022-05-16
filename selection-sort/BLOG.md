# **Selection Sort**

**Selection Sort** is a sorting algorithm that traverses the array several times while gradually constructing the sorting sequence. The traversal keeps track of the lowest value and inserts it at the front of the array, which should be sorted incrementally.

<br>

## **Pseudocode**

```
SelectionSort(arr):
    DECLARE n <-- len(arr)
    FOR i in range(1, n):
        j <-- i
        WHILE  arr[j-1] > arr[j] AND j>0:
            arr[j-1],arr[j] <-- arr[j], arr[j-1]
            j<-- j - 1
    RETURN  arr
```