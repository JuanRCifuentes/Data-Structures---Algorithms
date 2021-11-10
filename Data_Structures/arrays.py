# ----- Build an array
print('----- Create Array Class')

class MyArray:
    
    def __init__(self, data=[]):
        self.length = 0
        self.data = data
    
    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data.insert(self.length, item)
        self.length += 1
        return self.length

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        return lastItem

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        del self.data[self.length-1]
        self.length -= 1
        return item

    def shiftItems(self, index):
        i = index
        while(i < self.length-1):
            self.data[i] = self.data[i+1]
            i += 1

newArray = MyArray()
newArray.push('hi')
newArray.push('!')
newArray.push('you')
newArray.push('are')
newArray.push('nice')
newArray.push(':D')
# print(newArray.pop())

print(newArray.data)

newArray.delete(1)

print(newArray.data)
print(newArray.length)

# ----- REVERSE ARRAY -----
print('\n----- Reverse Array')

def checkIfString(input):
    if(not input or not isinstance(input, str)):
        return "gnirts a ton ,spoO"
    else:
        return input

def reverse(string):
    string = checkIfString(string)
    newString = ''
    for i in string:
        newString = newString + string[-1]
        string = string[:-1]
    return newString

def reverse2(string):
    string = checkIfString(string)
    return string[::-1]

print(reverse("j"))
print(reverse("juan"))
print(reverse(1))
print(reverse2("juan"))
print(reverse2(1))

# ----- MERGE SORTED ARRAYS -----
print('\n----- Merge Sorted Array')

def checkIfType(desiredType, message, parameters):
    for index, parameter in enumerate(parameters):
        assert type(parameter) == desiredType, message.format(index+1)

def mergeSortedArrays(array1, array2):
    try:
        checkIfType(list, 'Argument {} is not a list', [array1, array2])
    except AssertionError as e:
        print(e)
        return
    
    newArray = []

    # Inverted arrays so .pop() method complexity is 0(1) due to always deleting last item
    invArray1 = array1[::-1]
    invArray2 = array2[::-1]

    while(invArray1 and invArray2):
        item1 = invArray1.pop()
        item2 = invArray2.pop()
        try:
            checkIfType(int, 'Array {} has a non integer element to order', [item1, item2])
        except AssertionError as e:
            print(e)
            return
        if(item1 <= item2):
            newArray.append(item1)
            invArray2.append(item2)
        else:
            newArray.append(item2)
            invArray1.append(item1)

    newArray += invArray1
    newArray += invArray2

    print(newArray)

    return newArray

mergeSortedArrays([5,7,8,30], 33)
mergeSortedArrays([], [])
mergeSortedArrays([5,7,8,'a'], [4,6,30,40])
mergeSortedArrays([5,7,8,30], [4,6,30,40, 50, 55])