# Documentation

# Insert to Middle of an Array

You're asked to write a function that has two inputs or arguments, one is an array the other is a value and you have to return the input array but with the value added to its middle index while shifting the elements to the right.


## Whiteboard Process
![Whiteboard process for code challenge class 02](/code_challenge_class_02_array_insert_shift/array-insert-shift.jpg)


## Approach & Efficiency

The approach I took was to slice the array or list into two halves depending on the middle index, then add the value in the middle while shifting the elements to the right, as demonstrated in the Whiteboard Process


## Stretch Goal
Write a second function that removes an element from the middle index and shifts other elements in the array to fill the new gap.


```
def delete_shift_array(list):
    if type(value) == type([]):
        middle = int(len(list)/2) 
        new_list = list[:middle] + list[middle+1:]
        return new_list
    else:
        print("value is not an array, please change it into an array")
```