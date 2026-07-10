def add(a, b):
    """
    Takes two numbers and returns their sum.
    """
    return a + b


# ! For check message about error
def divide(a, b):
    """
    Divides a by b.
    Raises ValueError when dividing by zero.
    """
    if b == 0:
        raise ValueError("You can't divide by zero!")
    return a / b
