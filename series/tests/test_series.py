import pytest
from series.series import fibonacci

def test_fibonacci_at_5():
    assert fibonacci(5) == 5

def test_fibonacci_at_0():
    assert fibonacci(0) == 0
