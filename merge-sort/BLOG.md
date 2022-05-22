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

In this article, I'm going to be explaining **Merge Sort**

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

As the merge sort algorithm ***divides*** the given array/list into two halves, ***calls itself*** for the two halves and then ***merges*** the two sorted halves. Noting that, prior to the final merge of the sorted two halves, the initial two sub-lists are **divided** again and again into halves until the list cannot be divided any further. Then we combine the pair of one element lists into two-element lists, sorting them in the process. The sorted two-element pairs is merged into the four-element lists, and so on until we get the sorted list.




## Algorithm

