class Node:
    """
    - The __init__ method I have to consider the value the node contain,
    but since the node isn't added yet, then the node will point to None.
    - The __str__ I can choose the kind of representation I want to for each node I create.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """
    - The __init__ method: creates an empty queue when instantiated.
    with a property of a front and a rear node, but since the front and rear aren't added yet,
    they will point to None.
    - The __str__ I can choose the kind of representation I want to for each node I create.
    - The enqueue(): Changes the next property of the rear node to point to the node we are adding
     and re-assigns the rear reference or pointer to point to the node we are adding.
    - The dequeue(): Creates a temporary reference named temp and have it point to the same node
    that front is pointing too. And re-assigns front to the next value that the node front is pointing to.
    Also re-assigns the next property on the temp node to None.
    - The peek(): This method is for inspecting the front node of the queue.
    - The is_empty(): This method returns a True or False, based on the existance of a top node or not.
    (empty queue or not).
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        output = ""
        if self.front is None:
            output = "Empty Queue"
        else:
            current = self.front
            while current:
                output += f"{current.value} -> "
                current = current.next

            output += "None"
        return output

    def enqueue(self, value):
        node = Node(value)
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


class Dog:
    """
    a class for initializing a dog object for the animal shelter
    """
    def __init__(self):
        self.type = "dog"

    def __str__(self):
        return f"{self.type}"


class Cat:
    """"
    a class for initializing a cat object for the animal shelter
    """
    def __init__(self):
        self.type = "cat"

    def __str__(self):
        return f"{self.type}"


class AnimalShelter:
    """
    A class for enquing a dog or cat into the shelter according to FIFO approach,
    and dequeuing the animal according to the prefered animal.

    - enqueue method: enqueues a dog or cat into the shelter.
                      but if the animal is not an instance of dog or cat then raise an exception.
    - dequeue method: dequeues the animal according to the prefered animal.
                      but if the pref is not dog or cat then return the first animal in the shelter.

    - strech goal: if the pref is not dog or cat, then return the first added animal

    """
    def __init__(self):
        self.shelter = Queue()
        self.cat = Cat()
        self.dog = Dog()

    def __str__(self):
        return f"{self.shelter}"


    def enqueue(self, animal):

        # check if the animal is a dog or cat to enqueue it into the shelter, if not then raise an exception
        if not isinstance(animal, Dog) and not isinstance(animal, Cat):
            raise Exception("animal must be either a Cat or a Dog object")
        else:
            self.shelter.enqueue(animal)



    def dequeue(self, pref="butterfly"):

        if str(self.shelter.front.value) == pref:
            print("** the peek from if statment, when the peek == pref: ", self.shelter.peek())
            return self.shelter.dequeue()

        # strech goal: if the pref is not dog or cat, then return the first added animal
        if pref != "cat" and pref != "dog":
            print("** the peek from if statment, when the pref != cat or dog: ", self.shelter.peek())
            return self.shelter.dequeue()

        # incase if the self.shelter.peek() is not dog or cat, then traverse through the queue to reach the
        # first instance of the pref
        else:
            print("** the peek from else statment, when the peek != pref: ", self.shelter.peek())
            prev = None
            current = self.shelter.front
            while current:

                if str(current.value) == pref:
                    prev.next = current.next
                    current.next = None
                    return current.value
                prev = current
                current = current.next


if __name__ == "__main__":

    animal_shelter = AnimalShelter()

    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())
    animal_shelter.enqueue(Dog())
    animal_shelter.enqueue(Cat())

    print(animal_shelter.__str__())
    print("** dequeued: ", animal_shelter.dequeue("cat"))
    print(animal_shelter.__str__())
    print("** dequeued: ", animal_shelter.dequeue("dog"))
    print(animal_shelter.__str__())

    # strech goal: return the first added animal to the shelter when the pref is not dog or cat
    print("** dequeued: ", animal_shelter.dequeue("butterfly"))
    print(animal_shelter.__str__())
