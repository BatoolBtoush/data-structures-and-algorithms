from merge_sort.merge_sort import merge_sort


# Reverse-sorted: [20,18,12,8,5,-2]
def test_merge_sort():
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


# Few uniques: [5,12,7,5,5,7]
def test_merge_sort_few_uniques():
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


# Nearly-sorted: [2,3,5,7,13,11]
def test_merge_sort_nearly_sorted():
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_merge_sort_empty():
    actual = merge_sort([])
    expected = []
    assert actual == expected


# Negative & unsorted elements: [-2, -1, -3, -4, -5]
def test_merge_sort_negatives():
    actual = merge_sort([-2, -1, -3, -4, -5])
    expected = [-5, -4, -3, -2, -1]
    assert actual == expected

