# **Hashtables**

A hashtable is a data structure that stores key-value pairs. The key is used to retrieve the value. The value is the data that is stored. The key is a unique identifier for the value. The key is a string, integer, or other data type. The value can be any data type.


### **Terminology**

- **Hash:** A hash is the result of an algorithm that converts an entering string into a value that may be used for security or any other purpose. It is used to find the index of the array in the case of a hashtable.

- **Buckets:** A bucket is the content of each index in the hashtable's array. Each index corresponds to a bucket. If a collision happens, an index could include multiple key/value pairs.

- **Collisions:** A collision occurs When more than one key is hashed to the same place in the hashtable. For example, if the key "hello" is hashed to the index 3, and the key "world" is hashed to the index 3, then there is a collision.

<br>

## **Challenge**
You're asked to implement a ***HashTable*** Class with the following methods:

- **Hash Method**
    - **Arguments:** key
    - **Returns:** Index in the collection for that key

<br>

- **Set method**
    - **Arguments:** key, value
    - **Returns:** nothing
    - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    - Should a given key already exist, replace its value from the value argument given to this method.

<br>

- **Get Method**
    - **Arguments:** key
    - **Returns:** Value associated with that key in the table

<br>

- **Contains Method**
    - **Arguments:** key
    - **Returns:** Boolean, indicating if the key exists in the table already.

<br>

- **Keys Method**
    - **Returns:** Collection of keys

<br>

## **Approach & Efficiency**

**Approach:**

    - Create a HashTable class
    - Create a hash function
    - Create a set method
    - Create a get method
    - Create a contains method
    - Create a keys method
    And that the HashTable as a whole, is basically an array of buckets.


**Efficiency:**

    - Time Complexity: O(1) if it was a perfect hashtable (Best Case Scenario).
    But since there are chances of collision then it's O(n) (Average and Worst Case Scenario).
    - Space Complexity: O(n)



<br>

## **API**

- **Hash Method**
    - The hash method is a function that takes a key and calculates an index in the hashtable.



- **Set Method:**
    - The set method should hash the key using the **Hash Method** mentioned above, and set the key and value pair in the table, handling collisions as needed.
    - Should a given key already exist, replace its value from the value argument given to this method.

- **Get Method:**
    - The get method should hash the key using the **Hash Method** mentioned above, and return the value associated with that key in the table.

- **Contains Method:**
    - The contains method should hash the key using the **Hash Method** mentioned above, and return a boolean indicating if the key exists in the table already or not.

- **Keys Method:**
    - The keys method should return a collection of keys.