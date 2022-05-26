# **What Are Sorting Algorithms?**

Sorting algorithms are what we use to arrange the elements of an array aka list, in a specific order according to a comparison operator on the elements. The comparison operator is used to decide the new order of element in the respective data structure. The new order, could be of ascending, descending order, or even by alphabetical order.


![sorting-ascedning-order.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1653155983374/KI6u9fx7b.PNG align="left")

In this image we see that a sorting algorithm takes an array or list as an input, performs some kind of comparison operations on it and produce the sorted list in a specific order; ascendingly


## **The Importance of Sorting Algorithms**

Sorting Algorithms comes in handy when we have a specific aim to achieve while looking at a data structure, because as long as the given data structure is sorted or ordered in such a way, the process of getting what we want is made much easier and faster.

To sum it up in bullet-points, the importance of sorting algorithms are:

1. Searching for a specific element in a given array/list is much faster.

2. Selecting elements from an array/list based on their relation to the other elements of the same list is made easier.

3. Finding duplicate elements in an array/list is made easier and faster.

4. Analyzing the frequency distribution of the elements, meaning; which elements appear more or less in an array/list. Now is very fast with sorting algorithms.

## **Types of Sorting Algorithms:**
1. Insertion Sort
2. Merge Sort
3. Quick Sort
4. Selection Sort
5. Bubble Sort
6. Heap Sort
7. Radix Sort
8. Bucket Sort

In this article, I'm going to be explaining **Merge Sort** after I have explained [Insertion Sort](https://batoolragayah.hashnode.dev/sorting-algorithms-insertion-sort) before.

<br>

# **What is Meant By Merge Sort?**

Merge sort is an efficient sorting algorithm, that follows the *Divide and Conquer Algorithm*, which is considered to be a great resort for simplifying complicated problems.

<br>

## Defining Divide and Conquer Algorithm

As the name suggests, divide and conquer algorithm focuses on breaking down a complex problem into subproblems, solving those subproblems separately, then combining the solutions into a whole again, which will then help solve the main problem. 

In retrospect, this algorithm takes big use of recursion, which is usually expressed by a function calling itself to solve each subproblem until it reaches a base case.

The steps to the divide and conquer algorithm could be summarized in the following steps and image below:

- **Dividing:** Breaking down the complex problem into smaller sub-problems.
- **Conquering:** Solving the subproblems by taking use of recursion until they're solved.
- **Combining:** Merging the solution to the subproblems together to solve the main problem.

![Divide-&-Conquer-Algorithm.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1653155888064/R9nymMPyR.png align="left")

<br>

## Merge Sort Properties

<br>

## How Merge Sort Work?

After defining the divide and conquer algorithm, it is important to mention how identical the procedure is for the both of them. 

As the merge sort algorithm ***divides*** the given array/list into two halves, ***calls itself*** for the two halves and then ***merges*** the two sorted halves. Noting that, prior to the final merge of the sorted two halves, the initial two sub-lists are **divided** again and again into halves until the list cannot be divided any further. 

<br>

## Algorithm

1. Declare two functions; ***merge_sort()*** that is mainly responsible for splitting the main array into halves then later on, merges them by calling the other function; ***merge()***, which does the comparison of each sub-list element in each half to make sure to sort out those elements into their correct place.

2. In ***merge_sort()***, declare a variable to store the length of the list. Create an if statement, that if the length is greater than one, then "halve" the array into left and right.

3. Call  ***merge_sort()*** on each half (left and right) until they can no longer be halved, if so, call ***merge()*** on the the left, right and the array of that sub problem to sort it.

4. Inside ***merge()***, declare variables for indices in the left, right and the main array, to compare the values if they're greater or smaller and based on that comparison sort the elements in each sub-list until we get to the main list.

5. The latter can be done by declaring while loops and if/else statements.

6. Return the new array.

<br>

## Visualization of Merge Sort

As can be seen in the image below, this is how ***Merge Sort*** works, keeping in mind that because of the use of recursion we would always strive to reach a base case to stop the function calling, and in this algorithm the base case is; when the sub-list could no longer be halved.

![merge-sort-visual.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1653579028926/PV4-o1mFn.jpg align="left")

<br>

## Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)
   
   RETURN arr

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

    RETURN arr
``` 

<br>

## Python Code Implementation

```
def merge_sort(array):
    length = len(array)
    if length > 1:
        mid = length // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, array)
    return array


def merge(left, right, array):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        array[k:] = right[j:]
    else:
        array[k:] = left[i:]

    return array
``` 

<br>

## Efficiency And Big(O) Notation

**Big(O) Notation** is used to describe the efficiency of an algorithm or function. This efficiency is evaluated based on 2 factors:

- **Running Time (Time Complexity):** Which explains the amount of time a function or an algorithm needs to complete.

- **Memory Space (Space Complexity):** Explains the amount of memory resources a function or an algorithm uses to store data.

In order to analyze the above limiting factors, we should consider 4 key areas for analysis, which are:

1. Input Size
2. Units of Measurement
3. Orders of Growth
4. Best Case, Average Case, and Worst Case

Thus, the efficiency of any sorting algorithm is determined by the time and space complexities of the algorithm. And with merge sort it's no different, and they go as follows:




