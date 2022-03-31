from animal_shelter.animal_shelter import Node, Queue, AnimalShelter


def test_enqueue():
    animal_shelter = AnimalShelter()
    queue = Queue()

    animal_shelter.enqueue("kitty", "cat")
    actual = print(animal_shelter.enqueue("kitty", "cat"))
    excepted = "cat"
    assert actual == excepted
