from animal_shelter.animal_shelter import Node, Queue, AnimalShelter


def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("kitty", "cat")

    actual = animal_shelter.enqueue("kitty", "cat")
    excepted = 'cat'
    
    assert actual == excepted
