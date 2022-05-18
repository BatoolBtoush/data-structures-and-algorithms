def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = int(n / 2)
        left = arr[:mid]
        right = arr[mid:n]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    return arr


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    print(merge_sort([8, 4, 23, 42, 16, 15]))
    print(merge_sort([20, 18, 12, 8, 5, -2]))
    print(merge_sort([5, 12, 7, 5, 5, 7]))
    print(merge_sort([2, 3, 5, 7, 13, 11]))