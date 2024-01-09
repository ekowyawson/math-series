import pytest
from series.series import fibonacci,lucas,sum_series

"""
fibonacci tests
"""
def test_fibonacci_at_5():
    assert fibonacci(5) == 5

def test_fibonacci_at_0():
    assert fibonacci(0) == 0

"""
lucas tests
"""
def test_lucas_at_5():
    assert lucas(5) == 11

def test_lucas_at_0():
    assert lucas(0) == 2

def test_lucas_at_1():
    assert lucas(1) == 1

"""
sum_series tests
"""
def test_sum_series_at_0():
    assert sum_series(0) == 0

def test_sum_series_at_5_2_1():
    assert sum_series(5, 2, 1) == 11

def test_sum_series_at_5_3_2():
    assert sum_series(5, 3, 2) == 19

def test_sum_series_at_5():
    assert sum_series(5) == 5
