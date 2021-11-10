# ----- Build a hash table
print('----- Create Hash Table Class')

class MyHashTable:

    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for index, character in enumerate(key):
            hash = (hash + ord(character) * index) % len(self.data)
        return hash

    def set(self, key, value):
        index = self._hash(key)
        if(not self.data[index]):
            self.data[index] = []
        self.data[index].append([key, value])
        return self.data[index]

    def get(self, key):
        index = self._hash(key)
        currentBucket = self.data[index]
        if(currentBucket):
            for element in currentBucket:
                if(element[0] == key):
                    return element[1]
        return None
    
    def keys(self):
        keysArray = []
        for currentBucket in self.data:
            if currentBucket:
                # To prevent collision we loop through the bucket
                for element in currentBucket:
                    keysArray.append(element[0])
        return keysArray

myHashTable = MyHashTable(10)
print(myHashTable.set('grapes', 10))
print(myHashTable.get('grapes'))
print(myHashTable.set('apples', 9))
print(myHashTable.set('oranges', 5))
print(myHashTable.get('apples'))

print(myHashTable.data)
print(myHashTable.keys())

# ----- First Recurring Character Challenge

# Nested loops version
def firstRecurringCharacterFOR(input):
    for index, element1 in enumerate(input):
        i = 0
        while(i <= index-1):
            element2 = input[i]
            # print(f'First element: {element1}, Second element: {element2}')
            if(element1 == element2):
                return element1
            i += 1
    return None

# Hash table version
def firstRecurringCharacterHASH(input):
    temp = {}
    for element in input:
        if element in temp:
            return element
        else:
            temp[element] = True
        # print(temp)
    return None

print('\n----- First recurring character with loops')
print(firstRecurringCharacterFOR([2,5,1,2,3,5,1,2,4]))
print(firstRecurringCharacterFOR([2,1,1,2,3,5,1,2,4]))
print(firstRecurringCharacterFOR([2,3,4,5]))
print(firstRecurringCharacterFOR([]))

print('\n----- First recurring character with "hash tables" (dictionaries)')

print(firstRecurringCharacterHASH([2,5,1,2,3,5,1,2,4]))
print(firstRecurringCharacterHASH([2,1,1,2,3,5,1,2,4]))
print(firstRecurringCharacterHASH([2,3,4,5]))
print(firstRecurringCharacterHASH([]))