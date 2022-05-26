def quick_sort(array, left, right):
    if left < right:
        # Partition the array by setting the position of the pivot value
        position = partition(array, left, right)
        # Sort the left
        quick_sort(array, left, position - 1)
        # Sort the right
        quick_sort(array, position + 1, right)


def partition(array, left, right):
    # set a pivot value as a point of reference
    pivot = array[right]
    # create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1
    for i in range(left, right):
        if array[i] <= pivot:
            low += 1
            swap(array, i, low)
    # place the value of the pivot location in the middle.
    # all numbers smaller than the pivot are on the left, larger on the right.
    swap(array, right, low + 1)
    # return the pivot index point
    return low + 1


def swap(array, i, low):
    temp = array[i]
    array[i] = array[low]
    array[low] = temp


if __name__ == '__main__':
    array = [8,4,23,42,16,15]
    quick_sort(array, 0, len(array) - 1)
    print(array)