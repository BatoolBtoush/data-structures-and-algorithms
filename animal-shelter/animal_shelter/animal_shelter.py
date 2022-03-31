
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, node):
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty() == True:
            raise Exception("Nothing to dequeue from, the queue is empty!!")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.is_empty() == True:
            raise Exception("Nothing to peek at, the queue is empty!!")
        else:
            return self.front.value

    def is_empty(self):
        return self.front == None


class AnimalShelter:
    def __init__(self):
        self.cat= Queue()
        self.dog= Queue()
        

    def enqueue(self, animal, kind):
        if kind == 'cat':
            return self.cat.enqueue(animal)
        elif kind == 'dog':
            return self.dog.enqueue(animal)
        else:
            return "The aniaml is not a cat or a dog!"

    def dequeue(self, pref):
        if pref == 'dog':
            return self.dog.dequeue()
        if pref == 'cat':
            return self.cat.dequeue()
        else:
            return "The aniaml is not a cat or a dog!"


if __name__ == "__main__":

    animal_shelter = AnimalShelter()

    animal_shelter.enqueue("kitty", "cat")
    animal_shelter.enqueue("puppy", "dog")
    print(animal_shelter.enqueue("puppy", "dog"))
    animal_shelter.dequeue('cat')
    print(animal_shelter.dequeue('cat'))
