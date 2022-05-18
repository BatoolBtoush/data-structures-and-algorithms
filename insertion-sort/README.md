# **Challenge Summary**
Write a function **insertion_sort()** that takes in an unsorted array of integers and returns the same array sorted in ascending order.

<br>


## **Approach & Efficiency**


The insertion sort algorithm has 2 nested loops. And while the inner loop is considered to be efficient because it only goes through the list until it finds the correct position of an element. But still, the algorithm has an O(n^2) runtime complexity on the average scenario.

To explain each case or scenario of the **Time Complexity**:

- **Best Case Complexity**: This happens when the array or list is already sorted, only running the outer loop for n number of times while the inner loop is never executed. Thus, O(n).

- **Average Case Complexity**: This happens when the array elements are in jumbled order; meaning they're neither in ascending or descending. Thus, O(n^2)

- **Worst Case Complexity**: This happens when the array or list element are sorted in a reverse order of the order you're asked to sort them in, suppose the array is in descending order and you're asked to sort it in an ascending order. 
This would require executing the inner loop on every iteration to compare each element to the other elements.  Thus, O(n^2)

**Space Complexity:** 

The space complexity is of O(1). That's because in insertion sort, an extra variable key is used for swapping the list elements.

<br>


## **Solution**

The solution is found in the file `insertion_sort.py`.