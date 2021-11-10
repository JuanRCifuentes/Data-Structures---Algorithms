# Data Structures <!-- omit in toc -->

- [Summary](#summary)
  - [Languages](#languages)
  - [Operations and algorithms](#operations-and-algorithms)
- [Basic Data Structures](#basic-data-structures)
  - [Arrays](#arrays)
    - [Static vs. Dynamic](#static-vs-dynamic)
  - [Hash Tables](#hash-tables)
    - [Hash function](#hash-function)
    - [Buckets](#buckets)
    - [Collisions](#collisions)
    - [Excercises](#excercises)
- [How is data stored on a computer](#how-is-data-stored-on-a-computer)

## Summary 
**Data Structures:** Collection of values and have relations between them and functions. Each one have differences in what it can do and what it is best used for. 

There are different data structures as there are different kinds of containers in real life. For example, we have a briefcase for papers, but a fridge for food, but the fridge is not portable and uses a lot of energy. There are tons of Data Structures, but there are only about 5 useful ones to have always in mind.

The data structures has tradeoffs, some are good at certain operations,and some are good at others.

There are two important things to understand data structures:
1. How to build them
2. How to use them

### Languages
Each programming language has built in datatypes and data structures, and between them there may be differences even when speaking about the same data structure. Usually, languages have enough tools for us to create our own data structure.

### Operations and algorithms

- Insertion
- Deletion
- Traversal: Access each data item exactly once
- Searching
- Sorting
- Access
- Synamic programming
- BFS + DFS (Serching)
- Recursion

## Basic Data Structures
There are A LOT of data structures, but if we understand the basics, we should be able to understand the others.

- Arrays
- Stacks
- Queues
- Linked Lists
- Trees
- Tries
- Graphs
- Hash Tables

### Arrays

- Organizes data sequentially, one after the other in memory. 
- Smallest footprint
- Best choice for storing and iterating over every item

**OPARATIONS:**
| Lookup   | Push     | Insert   | Delete   |
|----------|----------|----------|----------|
| O(1)     | O(1)     | O(n)     | O(n)     |

> In file `arrays.py` we wrote a class called "MyArray" to understand how the basic methods for arrays work.

1. **Lookup [`O(1)`]:**
Because items are stored in memory and the program knows where each item is, to get an item using its index. `O(1)`

2. **Push [`O(1)`]:**
We are just inserting an element in the last place, we just need to add one item to the array. This results in placing one element in memory. Because we are dealing with dynamic arrays most of the time, this is not an issue... but when we are dealing with static arrays, this becomes `O(n)`. Sometimes even with dynamic arrays, as the grow the program eventually needs to copy the whole array into a new memory position with more reserved space, making it `O(n)`.

1. **Insert [`O(n)`]:**
To insert an item in a random location, we need to update the location of each item moved (or each item above the new one).

4. **Delete [`O(n)`]:**
Deleting an element means we have to update the location of each item moved after the deletion (or each item above the deleted one).

#### Static vs. Dynamic
Static arrays have a fixed length, we cannot add or append things. To change the length of the array, we have to create a new array with one more slot, copy every item from the previous array and finally place the new item. Some languages make this automatically, and this is called a Dynamic Array.


> **STRINGS ARE ARRAYS:** Strings are arrays of characters. 

**Exercise: Reverse a String** Function `reverse()` in file `arrays.py`.

### Hash Tables

- A hash table is a Data structure that uses a "Hash function" to find a place in memory for it's data. The Hash function converts the key into a number, and the language uses that number as the index in which the element is placed in memory.
- Elements are not sequencially placed in memory, as index is generated from the key and is almost a random number.
- Hash Tables need the keys to obtain it's elements.

PROS:
- Fast lookups (even when collisions occur)
- Fast inserts
- Flexible keys (keys could be any element, even functions)

CONS:
- Slow element iteration.
- Unordered

**OPERATIONS:**
| Lookup   | Push     | Insert   | Delete   |
|----------|----------|----------|----------|
| O(1)     | O(1)     | O(1)     | O(1)     |

> In file `hash_tables.py` we wrote a class called "MyHashTable" to understand how the basic methods for hash tables work.

1. **Lookup [`O(1)`]:**
Because items are stored in memory and the program knows where each item is (using the key), to get an item using its index. `O(1)`

2. **Push [`O(1)`]:**
To push an element into a hash table, it just needs to store the element in the place in memory dictated by the hash function (with the key).

3. **Insert [`O(1)`]:**
Inserting an element into a hash table means storing it in memory using the index dictated by the hash function (with the key). There is no need to update the index of the other items.

4. **Delete [`O(1)`]:**
To delete an element from a hash table, the functions needs to find the element using the hash funciton (with the key) and erase it from memory. There is no need to update the index of the other elements.

#### Hash function
- A Hash function usually returns a number given an element. 
- The number could be in a hexadecimal base. 
- The returned value is always the same for the same input.
- There are hash functions that recieve any kind of object, even functions.
- There are a LOT of hash functions such as "SHA-1" or "SHA-256".

**EXAMPLE:**
```javascript
_hash(key) {
  let hash = 0;
  for (let i =0; i < key.length; i++){
    hash = (hash + key.charCodeAt(i) * i) % maximum
  }
  return hash;
}
```
This hash function recieves a key and makes operations with each character (because the key is a string for this function) to finally return a number. The returned number cannot be higher than the variable maximum.


#### Buckets
A bucket is most commonly a type of data buffer or a type of document in which data is divided into regions.

#### Collisions
Because the index for each element in a hash table is given by the hash function and it can be repeated for multiple key values, there may be what is called a "collision". A collision means two or more elements are stored in the same bucket because the hash function returns the same index for those elements.

There are multiple ways to solve collisions.

One way to solve a collision, is allowing buckets to store multiple elements with it's keys. This means that the `get()` and `set()` methods for hash tables need a change to deal with collisions. Usually those methods simply iterate over the bucket to get every element stores insede them and this adds complexity to the functions. Because collisions rarely happen, complexity for `get()` and `set()` methods can be considered `O(1)`.

#### Excercises
Excercises are solved in file `hash_tables.py`.
1. Functions for the `MyHashTable` class:
     - Create hash table function `set(key, value)`. It must store the value and the key in the index dictated by the hash function `_hash(key)`. Returns the bucket in which the element is stored
     - Create hash table function `get(key)`. It must return the value of the requested key.
     - Create hash table function `keys()`. It must return an array with every key in the has table.
2. Function `firstRecurringCharacter(array)`. The function recieves an array of numbers and must return the first recurring character.
     - Using nested loops
     - Using hash tables

## How is data stored on a computer 

Variables in programs are located in RAM. Then when we save a file, it is located on long term storage. Long term storage is slower than RAM, that's why we use a volatile memory to use when we need quick access to data.

**Example:** When we run Google Chrome it creates variables and hold those in memory, but once we close Chrome, that variable is lost... so we save that in storage for later use. When Chrome loads next time, it takes data from the storage and place that into the RAM.

Bits are the smallest unit of storage in a PC. In real life these are tiny electrical switch that can be turned on or off. A bit can take two values `0` or `1` (`off` or `on` respectively). A byte is a collection ot 8 bits, an as so, it can have `2^8` values, or 256, ranging from `00000000` to `11111111`. Then there are the kilo, mega, giga, etc. metric prefixes. Systems with storage systems of 16, 32 or 64 bits, can have more values (`2^16`, `2^32` and `2^64` respectively). In JavaScript, as a number get too big, it eventually becomes `infinity`.

These units of storage, are inside the memory or the long time storage.

CPU is connected to a memory controller, which writes and reads over the storage. The controller has connections to all of the memory spaces individually assigned, so it has quick access to every pice of data stored. Thats why it is said we can access memory randomly... RAM, because we can get a random memory spot almost instantly. Still, the closer the information is, the faster a program can run. To increase even more the load speeds of some recent or vital information, the CPU have a small storage called `system cache` (example: lru cashe). 