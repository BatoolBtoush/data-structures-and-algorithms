from quick_sort.quick_sort import quick_sort

def test_quick_sort_reverse_sorted():
    array = [20, 18, 12, 8, 5, -2]
    quick_sort(array, 0, len(array) - 1)
    assert array == [-2, 5, 8, 12, 18, 20]


def test_quick_sort_empty_array():
    array = []
    quick_sort(array, 0, len(array) - 1)
    assert array == []


def test_quick_sort_one_element_array():
    array = [1]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1]

def test_quick_sort_two_element_array():
    array = [1, 2]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 2]

def test_quick_sort_three_element_array():
    array = [3, 2, 1]
    quick_sort(array, 0, len(array) - 1)
    assert array == [1, 2, 3]