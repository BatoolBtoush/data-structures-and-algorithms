def selection_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while arr[j-1] > arr[j] and j>0:
            arr[j-1],arr[j] = arr[j], arr[j-1]
            j -=1
    return arr




if __name__ == '__main__':
    arr = [8,4,23,42,16,15]
    print("array before sortion", arr)
    print("array after sortion", selection_sort(arr)) 
