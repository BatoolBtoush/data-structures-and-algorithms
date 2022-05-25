from hashtable.hashtable import HashTable
import pytest

# All tests are satisfied
# 1. Setting a key/value to your hashtable results in the value being in the data structure
# 2. Retrieving based on a key returns the value stored
# 3. Successfully returns null for a key that does not exist in the hashtable
# 4. Successfully returns a list of all unique keys that exist in the hashtable
# 5. Successfully handle a collision within the hashtable
# 6. Successfully retrieve a value from a bucket within the hashtable that has a collision
# 7. Successfully hash a key to an in-range value


# test hash method
def test_hash():
    hashtable = HashTable()
    actual = hashtable.hash("name")
    expected = 755
    assert actual == expected


# test set and get methods
def test_set_and_get(hashtable):
    assert hashtable.get("name") == "Batool Ragayah"
    assert hashtable.get("batool") == "ragayah"
    assert hashtable.get("course") == "Python"
    assert hashtable.get("abcdef") == "1"
    assert hashtable.get("bcdefa") == "2"
    assert hashtable.get("cdefab") == "3"
    assert hashtable.get("defabc") == "4"
    assert hashtable.get("doesnt exist") == None


# test contains method
def test_contains(hashtable):
    assert hashtable.contains("name") == True
    assert hashtable.contains("batool") == True
    assert hashtable.contains("Python") == False


# test keys method
def test_keys(hashtable):
    assert hashtable.keys() == [
        "abcdef",
        "bcdefa",
        "cdefab",
        "defabc",
        "course",
        "name",
        "batool",
    ]


@pytest.fixture
def hashtable():
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
    return hashtable
