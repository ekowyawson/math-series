# Lab: Class 02

## Project: Modules and Testing

Author: Ekow Yawson

### Links and Resources

---

- [In Tests We Trust - TDD with Python](https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932)
- [If name equals main](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/)
- [Recursion](https://www.geeksforgeeks.org/recursion/)
- [Python Modules and Packages](https://realpython.com/python-modules-packages/)

### Setup

---

**Requirements:**

- Install **pytest**: run `pip3 install pytest`

**Tests:**

- To run all tests, run the following command at the root of the project:

```bash
python -m pytest

# Or, if you are in a virtual env i.e., venv:
pytest
```

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

- [x] **Create a module `series.py`.**

- [x] **Add a file `test_series.py` to your repository.**
  - As you work on the tasks below, use **TDD (Test-Driven Development) practices**:
    - Write tests first, then implement code.
    - Make small changes with many cycles of _Red-Green-Refactor_.

- [x] **Create a function called `fibonacci`.**
  - [x] The function should have one parameter `n`.
  - [x] The function should return the `nth` value in the Fibonacci series.
  - [x] Implement the function using **recursion** or **iteration**.
  - [x] Ensure that your function(s) have a well-formed docstring.

- [x] **In your `series.py` module, add a new function called `lucas` that returns the `nth` value in the Lucas numbers.**
  - Again, you may use recursion or iteration, or both. Ensure that your function has a well-formed docstring.
  - Both the Fibonacci series and the Lucas numbers are based on an identical formula.

- [x] **Add a third function called `sum_series` with one required parameter and two optional parameters.**
  - [x] The required parameter will determine which element in the series to print.
  - [x] The two optional parameters will have default values of `0` and `1` and will determine the first two values for the series to be produced.
  - [x] Calling this function with no optional parameters will produce numbers from the Fibonacci series.
  - [x] Calling it with the optional arguments `2` and `1` will produce values from the Lucas numbers.
  - [x] Other values for the optional parameters will produce other series.

- [x] **Test all three functions.**

- [x] Add your `series.py` and `test_series.py` modules to your repository and commit frequently while working on your implementation.
  - Include good commit messages that explain concisely both what you are doing and why.

---
