from hashmap_left_join.hashmap_left_join import left_join, HashTable

def test_HashTable_left_join():
    HashTable1 = HashTable()
    HashTable1.set('fond', 'enamored')
    HashTable1.set('wrath', 'anger')
    HashTable1.set('diligent', 'employed')
    HashTable1.set('outfit', 'garb')
    HashTable1.set('guide', 'usher')

    HashTable2 = HashTable()
    HashTable2.set('fond', 'averse')
    HashTable2.set('wrath', 'delight')
    HashTable2.set('diligent', 'idle')
    HashTable2.set('guide', 'follow')
    HashTable2.set('flow', 'jam')

    assert left_join(HashTable1, HashTable2) == left_join(HashTable2, HashTable1)