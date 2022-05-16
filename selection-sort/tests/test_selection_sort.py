from selection_sort.selection_sort import selection_sort


#Reverse-sorted 
def test_selection_sort_1():
    actual = selection_sort([20,18,12,8,5,-2])
    expected =  [-2, 5, 8, 12, 18, 20]
    assert actual == expected


#Few uniques
def test_selection_sort_2():
    actual = selection_sort([5,12,7,5,5,7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


#Nearly-sorted
def test_selection_sort_3():
    actual = selection_sort([2,3,5,7,13,11])
    expected =  [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_selection_sort_4():
    actual = selection_sort([2,0,-2,3,90,12])
    expected = [-2, 0, 2, 3, 12, 90]
    assert actual == expected
