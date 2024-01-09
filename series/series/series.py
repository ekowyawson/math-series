def fibonacci(n):
    """Return the nth value in the Fibonacci series."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
