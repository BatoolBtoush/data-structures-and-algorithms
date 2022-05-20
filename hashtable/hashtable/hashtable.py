class HashaTable(object):
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
                    self.map[index][i] = [key, value]
                    return
            self.map[index].append([key, value])

    def get(self, key):
        """
        This method takes a type string (key) and returns the value associated with that key.
        """
        index = self.hash(key)
        return self.map[index][0][1]

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
        


if __name__ == "__main__":
    hashtable = HashaTable()

    hashtable.set("name", "Batool Ragayah ")  # 755
    hashtable.set("batool", "ragayah")  # 915
    hashtable.set("course", "js")  # 195
    hashtable.set("course", "Python")  # 195

    hashtable.set("abcdef", "1")  # 79
    hashtable.set("bcdefa", "2")  # 79
    hashtable.set("cdefab", "3")  # 79
    hashtable.set("defabc", "4")  # 79


    print(hashtable.get("name"))  # "Ragayah Batool"


    print(hashtable.contains("name"))  # True
    print(hashtable.contains("batool"))  # True
    print(hashtable.contains("python"))  # True


    print(hashtable.keys())  # ['name', 'batool', 'course', 'abcdef', 'bcdefa', 'cdefab', 'defabc']







# # for printing
# for item in enumerate(hashtable.map):
#     if item is not None:
#         print(item)


# batool
# print(12179%1024)

# #course
# print(12483%1024)

# print(11343%1024)
