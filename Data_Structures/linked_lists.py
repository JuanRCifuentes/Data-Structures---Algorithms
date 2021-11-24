class MyNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def pointTo(self, node):
        self.next = node
    
    def __str__(self):
        return str(f'{self.value} --> {self.next}')

class MyLinkedList:

    def __init__(self, value):
        self.head = MyNode(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = MyNode(value)
        self.tail.pointTo(newNode)
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = MyNode(value)
        newNode.pointTo(self.head)
        self.head = newNode
        self.length += 1

    def traverseToIndex(self, index):
        currentNode = self.head
        i = 0
        while(i < index and index < self.length):
            currentNode = currentNode.next
            i += 1

        return currentNode

    def insert(self, index, value):

        if (index == 0):
            self.prepend(value)
            return
        elif (index >= self.length):
            self.append(value)
            return
        
        newNode = MyNode(value)
        nodeBefore = self.traverseToIndex(index-1)
        
        newNode.pointTo(nodeBefore.next)
        nodeBefore.pointTo(newNode)

        self.length += 1
    
    def remove(self, index):
        nodeBefore = self.traverseToIndex(index-1)
        nodeToDelete = nodeBefore.next 
        nodeBefore.pointTo(nodeToDelete.next)
        if (index+1 >= self.length):
            self.tail = nodeBefore
        del nodeToDelete
        self.length -= 1

    def reverse(self):
        prevNode = None
        currentNode = self.head
        nextNode = currentNode.next

        while(nextNode):
            tempNode = nextNode.next
            nextNode.pointTo(currentNode)
            currentNode.pointTo(prevNode)
            prevNode = currentNode
            currentNode = nextNode
            nextNode = tempNode

        self.head, self.tail = self.tail, self.head

    # Function for the class to return something readable
    def __str__(self):
        return str(self.head)

myLinkedList = MyLinkedList(10)
print(myLinkedList)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
print(myLinkedList)
myLinkedList.insert(2, 4)
print(myLinkedList)
myLinkedList.insert(6, 3)
print(myLinkedList)
myLinkedList.remove(1)
print(myLinkedList)
myLinkedList.remove(4)
print(myLinkedList)

myLinkedList.reverse()
print(myLinkedList)

# ----- Pointers
def pointers():
    object = { 'a': True }
    pointer = object

    object['a'] = 'booya'

    del object

    print(f'The pointer value is: {pointer}')
    # print(f'The object value is: {object}') # This sends an error because the variable `object` was deleted

pointers()