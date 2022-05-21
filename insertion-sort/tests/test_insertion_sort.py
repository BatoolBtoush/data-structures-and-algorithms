from insertion_sort.insertion_sort import insertion_sort


# Reverse-sorted: [20,18,12,8,5,-2]
def test_insertion_sort_reverse_sorted():
    actual = insertion_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


# Few uniques: [5,12,7,5,5,7]
def test_insertion_sort_few_uniques():
    actual = insertion_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


# Nearly-sorted: [2,3,5,7,13,11]
def test_insertion_sort_nearly_sorted():
    actual = insertion_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


# Sorted: [0,1,2,3,4,5]
def test_selection_sort_sorted():
    actual = insertion_sort([0, 1, 2, 3, 4, 5])
    expected = [0, 1, 2, 3, 4, 5]
    assert actual == expected


# [2,0,-2,3,90,12]
def test_selection_sort_one():
    actual = insertion_sort([2, 0, -2, 3, 90, 12])
    expected = [-2, 0, 2, 3, 12, 90]
    assert actual == expected


# [8,4,23,42,16,15]
def test_selection_sort_two():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
