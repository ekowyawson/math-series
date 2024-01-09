"""
The Fibonacci sequence is a series of numbers where a number is
the addition of the last two numbers, starting with 0, and 1.
"""

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The index of the Fibonacci number to calculate.
                 Indices start at 0.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not if type integer.

    Returns:
        int: The nth Fibonacci number.

    Examples:
        >>> fibonacci(5)
        5
        >>> fibonacci(0)
        0
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be of type integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


"""
The Lucas numbers are an integer sequence similar to the Fibonacci sequence, 
where each number is the sum of the two preceding numbers, starting with 2 and 1.
"""

def lucas(n):
    """Calculate the nth Lucas number using recursion.

    Args:
        n (int): The index of the Lucas number to calculate.
                 Indices start at 0.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not if type integer.

    Returns:
        int: The nth Lucas number.

    Examples:
        >>> lucas(5)
        5
        >>> lucas(0)
        0
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be of type integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


# Using iteration
def sum_series(n, num1 = 0, num2 = 1):
    """Calculate the nth value of a series (of sums).

    This function generalizes the Fibonacci and Lucas numbers
    to work with any first two numbers. By default, the function
    produces Fibonacci series values.

    Args:
        n (int): The index of the element in the series to retrieve.
        first (int, optional): The first term in the series with a default value of 0.
        second (int, optional): The second term in the series with a default value of 1.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If any argument is not if type integer.

    Returns:
    int: The nth element in the series.

    Examples:
    >>> sum_series(5)
    5
    >>> sum_series(5, 2, 1)
    11
    >>> sum_series(5, 3, 2)
    19
    """
    if not all(isinstance(arg, int) for arg in (n, num1, num2)):
        raise TypeError("All arguments must be integers")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return num1
    elif n == 1:
        return num2
    else:
        for _ in range(n - 1):
            num1, num2 = num2, num1 + num2
        return num2