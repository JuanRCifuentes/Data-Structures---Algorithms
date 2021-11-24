class MyNode:

    def __init__(self, value, previousNode=None, nextNode=None):
        self.value = value
        self.next = nextNode
        self.previous = previousNode

    def pointToNext(self, nextNode):
        self.next = nextNode

    def pointToPrevious(self, previousNode):
        self.previous = previousNode

    
    def __str__(self):
        lineBreak = '\n'
        previousValue = 'None' if self.previous==None else self.previous.value
        nextValue = 'None' if self.next==None else self.next.value
        currentValue = f'<-- {self.value} -->'
        textLine = '{:<5}  {:5}  {:>5}'.format(previousValue, currentValue.center(15), nextValue)
        next = '' if self.next==None else self.next
        return f'{textLine}{lineBreak}{next}'
        
class MyLinkedList:

    def __init__(self, value):
        self.head = MyNode(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        oldTail = self.tail
        newNode = MyNode(value, oldTail, None)
        oldTail.pointToNext(newNode)
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        oldHead = self.head
        newNode = MyNode(value, None, oldHead)
        oldHead.pointToPrevious(newNode)
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
        nodeAfter = nodeBefore.next
        
        nodeBefore.pointToNext(newNode)
        newNode.pointToNext(nodeAfter)
        newNode.pointToPrevious(nodeBefore)
        nodeAfter.pointToPrevious(newNode)

        self.length += 1
    
    def remove(self, index):
        nodeToDelete = self.traverseToIndex(index)
        nodeBefore = nodeToDelete.previous
        nodeAfter = nodeToDelete.next

        if (index == 0):
            nodeAfter.pointToPrevious(nodeBefore)
            self.head = nodeAfter
        elif (index+1 == self.length):
            nodeBefore.pointToNext(nodeAfter)
            self.tail = nodeBefore
        else:
            nodeBefore.pointToNext(nodeAfter)
            nodeAfter.pointToPrevious(nodeBefore)
            
        del nodeToDelete
        self.length -= 1

    # Function for the class to return something readable
    def __str__(self):
        lineBreak = "\n"
        return str(self.head)

myLinkedList = MyLinkedList(100)
print(myLinkedList, f'The list length is: {myLinkedList.length}', "\n")
myLinkedList.append(5)
myLinkedList.append(160)
print(myLinkedList, f'The list length is: {myLinkedList.length}', "\n")
myLinkedList.prepend(1)
print(myLinkedList, f'The list length is: {myLinkedList.length}', "\n")
myLinkedList.insert(2, 4)
myLinkedList.insert(6, 3)
print(myLinkedList, f'The list length is: {myLinkedList.length}', "\n")
myLinkedList.remove(1)
myLinkedList.remove(4)
print(myLinkedList, f'The list length is: {myLinkedList.length}', "\n")