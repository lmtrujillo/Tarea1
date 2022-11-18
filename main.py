# TAREA 1
# LUIS MARIO TRUJILLO AGUILAR
# A01209150

# CLASS STACK
class Stack:
    def __init__(self) -> None:
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()
        else:
            return "Empty stack"


# Stack testing
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


# CLASS QUEUE
class Queue:
    def __init__(self) -> None:
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)
        else:
            return "Empty queue"


# Stack testing
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())


# CLASS HASH TABLE
class HashTable:
    def __init__(self) -> None:
        self.array = [None] * 1000

    def hash_function(self, key):
        length = len(self.array)
        # Get a hash value that fits the length
        return hash(key) % length

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check is element if already on the array
        if self.array[index] is not None:
            # Check is element if has exactly same key
            for element_to_update in self.array[index]:
                if element_to_update[0] == key:
                    element_to_update[1] = value
                    break
                else:
                    self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        # Check is element if found on the array
        if self.array[index] is None:
            return "Element not found"
        else:
            # Check if element has same key
            for element_found in self.array[index]:
                if element_found[0] == key:
                    return element_found[1]

            return "Element not found"


# Hash Table testing
hashTable = HashTable()
hashTable.insert(1, "Luis")
hashTable.insert(2, "Jose")
print(hashTable.search(1))
print(hashTable.search(2))
hashTable.insert(1, "Luis Mario")
print(hashTable.search(1))
print(hashTable.search(3))
