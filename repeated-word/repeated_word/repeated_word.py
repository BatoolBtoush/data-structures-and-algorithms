import string


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


def first_repeated(string):
    """
    This method takes a string as an argument and returns the first word that occurs more than once in the string.
    """
    hashtable = HashTable()
    first_repeated = ""
    # print(string)
    lowered = string.lower()
    # print(lowered)
    replaced = (
        lowered.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ")
    )
    # print(replaced)
    splitted = replaced.split()
    # print(splitted)
    for word in splitted:
        if hashtable.contains(word):
            if first_repeated == "":
                first_repeated = word
                # for item in enumerate(hashtable.map):
                #     if item is not None:
                #         print(item)
            return first_repeated
        else:
            hashtable.set(word, None)


if __name__ == "__main__":
    hashtable = HashTable()

    print(first_repeated("Once upon a time, there was a brave princess who..."))
    print(
        first_repeated(
            "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
        )
    )
    print(
        first_repeated(
            "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
        )
    )

    print(first_repeated("first nice! blah first, whatever blah nice whatever.."))
    print(first_repeated("nice cool?? nice blah cool whatever blah nice.. whatever"))
