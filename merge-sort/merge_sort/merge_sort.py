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


if __name__ == "__main__":
    array = [8, 4, 23, 42, 16, 15]
    print(merge_sort(array))
