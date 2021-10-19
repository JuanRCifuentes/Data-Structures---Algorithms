# Big O Cheat Sheet

# Big O's
- O(1): Constant - No loops
- O(log(n)): Logarithmic - Usually searching algorithms have log(n) if they are sorted (Binary Search)
- O(n): Linear - Loops and searching algorithms when not sorted.
- O(n*log(n)): Log Linear - Sorting operations usually
- O(n^2): Quadratic - Every element needs to be compared to every other element. Two nested loops
- O(2^n): Exponential - Recursive algorithms
- O(n!): Factorial - Adding a loop for every element

** Iterating though half of a collection is still O(n)

** Two separate collections: 
    - O(a+b) When one after the other
    - O(a*b) When nested

# What Cause time in a function?

- Operations (+, -, *, /, etc.)
- Comparisons (<, >, ==, etc.)
- Looping (for, while)
- Outside funciton calling (function())

# Rulebook
- Rule 1: Always worst case
- Rule 2: Remove constants
- Rule 3: Different inputs should have different variables. + for steps in order, * for nested steps
- Rule 4: Drop non dominants