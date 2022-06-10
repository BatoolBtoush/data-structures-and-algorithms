from hashmap_left_join.hashmap_left_join import left_join, HashTable


def test_hashmap_left_join():
    hashmap1 = HashTable()
    hashmap1.set("diligent", "employed")
    hashmap1.set("fond", "enamored")
    hashmap1.set("guide", "usher")
    hashmap1.set("outfit", "garb")
    hashmap1.set("wrath", "anger")

    hashmap2 = HashTable()
    hashmap2.set("diligent", "idle")
    hashmap2.set("fond", "averse")
    hashmap2.set("guide", "follow")
    hashmap2.set("flow", "jam")
    hashmap2.set("wrath", "delight")

    new_hashmap = left_join(hashmap1, hashmap2)
    actual = new_hashmap.get("diligent")
    expected = ["employed", "idle"]
    assert actual == expected

    actual = new_hashmap.get("outfit")
    expected = ["garb", None]
    assert actual == expected


def test_hashmap_left_join_2():
    hashmap1 = HashTable()
    hashmap1.set("light", "brightness")
    hashmap1.set("thin", "slim")
    hashmap1.set("right", "correct")
    hashmap1.set("happy", "joyful")

    hashmap2 = HashTable()
    hashmap2.set("light", "darkness")
    hashmap2.set("thin", "thick")
    hashmap2.set("right", "wrong")
    hashmap2.set("full", "empty")

    new_hashmap = left_join(hashmap1, hashmap2)
    actual = new_hashmap.get("light")
    expected = ["brightness", "darkness"]
    assert actual == expected

    actual = new_hashmap.get("happy")
    expected = ["joyful", None]
    assert actual == expected

def test_empty_hashmap():
    hashmap1 = HashTable()
    hashmap2 = HashTable()

    new_hashmap = left_join(hashmap1, hashmap2)
    actual = new_hashmap.keys()
    expected = []
    assert actual == expected