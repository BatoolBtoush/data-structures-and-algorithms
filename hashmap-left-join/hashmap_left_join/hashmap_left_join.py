# Write a function called left join
# Arguments: two hash maps
# The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
# The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
# Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
# NOTES:

# Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
# LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
# If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.


class HashTable(object):
    def __init__(self, size=1024):

        self.size = size
        self.map = [None] * size

    def hash(self, key):
        """
        This method takes an argument of type string (key) and returns an integer value (hash value) which
        is the index  of the key in the table.
        """
        sum_of_ascii = 0
        for char in key:
            char_ascii = ord(char)
            sum_of_ascii += char_ascii
        hashed_key = (sum_of_ascii * 19) % self.size

        return hashed_key

    def set(self, key, value):
        """
        This method takes two arguments:
        1. A type string (key)
        2. Value

        This method does the following tasks:
        - hash the key by calling the hash method
        - set the key and value pair in the table, while handling collisions
        - checks if the key is already in the table, and if so it would update the value for that key to the value
            provided in the method's parameter

        """
        index = self.hash(key)
        if self.map[index] is None:
            self.map[index] = [[key, value]]
        else:
            # check if key is already in the table
            # if so, update the value for that key to the value provided in the method's parameter
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    self.map[index][i][1] = value
                    return
            self.map[index].append([key, value])

    def get(self, key):
        """
        This method takes a type string (key) and returns the value associated with that key.
        """
        index = self.hash(key)
        if self.map[index] is None:
            return None
        else:
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    return self.map[index][i][1]
            return None

    def contains(self, key):
        """
        This method takes a type string (key) and returns a Boolean:
        True if the key is in the table, and False otherwise.
        """
        index = self.hash(key)
        if self.map[index] is None:
            return False
        else:
            for i in range(len(self.map[index])):
                if self.map[index][i][0] == key:
                    return True
            return False

    def keys(self):
        """
        This method returns a collection of all keys in the table.
        """
        keys = []
        for i in range(len(self.map)):
            if self.map[i] is not None:
                for j in range(len(self.map[i])):
                    keys.append(self.map[i][j][0])
        return keys


def left_join(hashmap1, hashmap2):
    """
    This method takes two hashmaps as arguments and returns a new hashmap
    that is a left join of the two hashmaps.

    if no values exist in the right hashmap, then some flavor of None should be appended to the result row.
    """
    if not hashmap1 or not hashmap2:
        return None

    new_hashmap = HashTable()
    for key in hashmap1.keys():
        new_hashmap.set(key, hashmap1.get(key))

    for key in hashmap2.keys():
        if new_hashmap.contains(key):
            new_hashmap.set(key, new_hashmap.get(key) + ',' + hashmap2.get(key))
        else:
            new_hashmap.set(key, hashmap2.get(key))

    for item in enumerate(new_hashmap.map):
        if item is not None:
            print(item)

    

if __name__ == "__main__":
    hashmap1 = HashTable()
    hashmap1.set('fond', 'enamored')
    hashmap1.set('wrath', 'anger')
    hashmap1.set('diligent', 'employed')
    hashmap1.set('outfit', 'garb')
    hashmap1.set('guide', 'usher')

    hashmap2 = HashTable()
    hashmap2.set('fond', 'averse')
    hashmap2.set('wrath', 'delight')
    hashmap2.set('diligent', 'idle')
    hashmap2.set('guide', 'follow')
    hashmap2.set('flow', 'jam')

    left_join(hashmap1, hashmap2)
    # for printing
# for item in enumerate(hashmap1.map):
#     if item is not None:
#         print(item)

# for item in enumerate(hashmap2.map):
#     if item is not None:
#         print(item)






