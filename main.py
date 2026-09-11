"""
Main module for test-autolink-functionality.

This module contains example functions to demonstrate automated Sphinx documentation.
"""


def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet.
        
    Returns:
        A greeting message.
        
    Examples:
        >>> greet("World")
        'Hello, World!'
    """
    return f"Hello, {name}!"


def calculate_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two numbers.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        The sum of a and b.
        
    Examples:
        >>> calculate_sum(2, 3)
        5
    """
    return a + b


def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        x: First number.
        y: Second number.
        
    Returns:
        The product of x and y.
        
    Examples:
        >>> multiply(2.0, 3.0)
        6.0
    """
    return x * y


def divide(x: float, y: float) -> float:
    """
    Divide two numbers.
    
    Args:
        x: Numerator.
        y: Denominator.
        
    Returns:
        The quotient of x divided by y.
        
    Raises:
        ZeroDivisionError: If y is zero.
        
    Examples:
        >>> divide(10.0, 2.0)
        5.0
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {calculate_sum(2, 3)}")
    print(f"10 / 2 = {divide(10.0, 2.0)}")
