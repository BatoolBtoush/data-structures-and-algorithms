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


def repeated_word(text):
    """
    This function takes a string and it finds the first repeated word to occur more than once in a string    
    """
    # create a hash table
    table = HashTable()
    lis = []
    # split the string into words
    words = text.split()
    # loop through the words
    for word in words:
        # check if the word is in the table
        if table.contains(word):
            # if so, add the word to the list
            lis.append(word)
            if len(lis) > 1:
                return lis[0]
        else:
            # if not, add the word to the table
            table.set(word, word)
    # if no word is found, return None
    return None


if __name__ == "__main__":
    hashtable = HashTable()

    hashtable.set("name", "Batool Ragayah")  # 755
    hashtable.set("batool", "ragayah")  # 915
    hashtable.set("course", "js")  # 195
    hashtable.set("course", ".net")  # 195
    hashtable.set("course", "Python")  # 195

    hashtable.set("abcdef", "1")  # 79
    hashtable.set("bcdefa", "2")  # 79
    hashtable.set("cdefab", "3")  # 79
    hashtable.set("defabc", "4")  # 79

    print(repeated_word("Once upon a time, there was a brave princess who..."))
    print(
        repeated_word(
            "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
        )
    )
    print(
        repeated_word(
            "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
        )
    )
