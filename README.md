# Data Structures and Algorithms <!-- omit in toc -->

- [What is good code ?](#what-is-good-code-)
  - [Time Complexity - Big O](#time-complexity---big-o)
  - [Space Complexity](#space-complexity)
    - [What causes space complexity ?](#what-causes-space-complexity-)
    - [Examples](#examples)
- [Data Structures](#data-structures)

## What is good code ?
1. **Readable**
2. **Scalable**
   - **Time complexity - Big O Notation:**  Instructions must be efficient, so as the number of inputs increase, the program doesn't constantly slow down.
   - **Space Complexity - Memory:** When computers were being born, memory was very expensive. Nowadays not as much but it is limited, not infinite...

Three pillars or programming:
1. Readable
2. Memory - Space Complexity
3. Speed - Time Complexity

### Time Complexity - Big O

[Link to section](BIG_O/README.md)

If the functions we create are gonna be used only for small inputs, Big O doesn't matter at all, but that's not real world. When things go big, code gets out of hand.

Every method has a cost, even predetermined methods, like `unshift()` in JavaScript, which is O(n). This helps us choose the better methods or data structures for our usecase.

Programs = Data Structures + Functions, and a great programmer must be able to choose the correct Data Structure and the right algorithm to write a program.

This sections will give a tool to choose a function according to it's scalability.

### Space Complexity

Compare the total size relative to the size of the input and see how many new variables or mamory is being used. When we have limited memory and add more that it can take, it may overflow... (stack overflow !). 

We don't include space taking up by the input

#### What causes space complexity ?

- Variables
- Data structures
- Function call
- Allocations

#### Examples

```javascript
function booooo(n){
    for (let i=0, i<n.length; i++) {
        console.log('booooo!');
    }
}

booooo([1, 2, 3, 4, 5]);
```
This function created an index for the loop, so it has a Space complexity O(1).

```javascript
function function1(n){
    let hiArray = [];
    for (let i=0, i<n.length; i++) {
        hiArray[i] = 'hi';
    }
    return hiArray;
}

function2(6)
```
This function created an array, the index variable and an item in the array for each input, so it has a Space Complexity O(n).

## Data Structures

[Link to section](Data_Structures/README.md)

Data Structures are a fundamental to know. 

Collection of values and have relations between them and functions. Each one have differences in what it can do and what it is best used for. 