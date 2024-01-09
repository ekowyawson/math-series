# Lab: Class 02

## Project: Modules and Testing

Author: Ekow Yawson

### Overview

---

#### The Fibonacci Series

The **Fibonacci Series** is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:

`0, 1, 1, 2, 3, 5, 8, 13, ...`

Note When asking for the `nth` number in series presume starting at zero.

`fibonacci(0) == 0`, `fibonacci(1) == 1`, `fibonacci(2) == 1`, etc.

#### The Lucas Numbers

The **Lucas Numbers** are a related series of integers that start with the values
**2** and **1** rather than 0 and 1. The resulting series looks like this:

`2, 1, 3, 4, 7, 11, 18, 29, ...`

### Feature Tasks and Requirements

---

1. Create a module `series.py`.
2. Add a file `test_series.py` to your repository.
   - As you work on the tasks below, use **TDD (Test-Driven Development) practices**:
     - Write tests first, then implement code.
     - Make small changes with many cycles of Red-Green-Refactor.
3. Create a function called `fibonacci`.
   - The function should have one parameter `n`.
   - The function should return the `nth` value in the Fibonacci series.
   - You may implement the function using **recursion** or **iteration**.
     - If you are feeling particularly frisky, do both as separate functions.
   - Ensure that your function(s) has a well-formed docstring.
4. In your `series.py` module, add a new function called `lucas` that returns the `nth` value in the Lucas numbers. Again, you may use recursion or iteration, or both. Ensure that your function has a well-formed docstring.
   - Both the fibonacci series and the lucas numbers are based on an identical formula.
5. Add a third function called `sum_series` with **one required parameter** and **two optional parameters**.
   - The required parameter will determine which element in the series to print.
   - The two optional parameters will have default values of `0` and `1` and will determine the first two values for the series to be produced.
   - Calling this function with no optional parameters will produce numbers from the fibonacci series.
   - Calling it with the optional arguments `2` and `1` will produce values from the lucas numbers.
   - Other values for the optional parameters will produce other series.
   - Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.
6. Add your `series.py` and `test_series.py` modules to your repository and commit frequently while working on your implementation.
   - Include good commit messages that explain concisely both what you are doing and why.

---
