def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key_element = array[i]
        left_to_the_key_element = i - 1
        while left_to_the_key_element >= 0 and key_element < array[left_to_the_key_element]:
            array[left_to_the_key_element + 1] = array[left_to_the_key_element]
            left_to_the_key_element -= 1
        array[left_to_the_key_element + 1] = key_element

    return array

if __name__ == '__main__':
    arr = [8,4,23,42,16,15]
    print("array before sortion", arr)
    print("array after sortion", insertion_sort(arr)) 
