from animal_shelter.animal_shelter import Node, Queue, AnimalShelter, Dog, Cat
import pytest


def test_enqueuing_into_the_shelter(animal_shelter):
    actual = animal_shelter.__str__()
    excepted = "dog -> dog -> cat -> dog -> cat -> dog -> cat -> None"
    assert actual == excepted


def test_front_or_peek_of_the_shelter(animal_shelter):
    actual = str(animal_shelter.shelter.front.value)
    expected = "dog"
    assert actual == expected


# dequeue from shelter when the peek = pref
def test_dequeuing_from_the_shelter(animal_shelter):
    animal_shelter.dequeue("dog")
    actual = animal_shelter.__str__()
    expected = "dog -> cat -> dog -> cat -> dog -> cat -> None"
    assert actual == expected


# dequeu from shelter when the peek != pref
def test_dequeuing_from_the_shelter_when_peek_is_not_pref(animal_shelter):
    animal_shelter.dequeue("cat")
    actual = animal_shelter.__str__()
    expected = "dog -> dog -> dog -> cat -> dog -> cat -> None"
    assert actual == expected


# dequeue from shelter when the pref is not dog or cat
def test_dequeuing_from_the_shelter_when_pref_is_not_dog_or_cat(animal_shelter):
    animal_shelter.dequeue("butterfly")
    actual = animal_shelter.__str__()
    expected = "dog -> cat -> dog -> cat -> dog -> cat -> None"
    assert actual == expected


@pytest.fixture()
def animal_shelter():
    animal_shelter = AnimalShelter()

    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())

    return animal_shelter
