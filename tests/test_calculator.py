import pytest

from src.calculator import add, divide


def test_add():
    # Using assert to check
    assert add(2, 3) == 5


# def test_add_with_wrong_expectation():
#     """
#     # ! Failed test for example
#     This test is specifically designed to fail.
#     """
#     # Call a function directly inside an assert to see the error details
#     assert add(2, 2) == 5


def test_add_raises_type_error_on_string_input():
    """
    # ! Example how to testing exceptions
    """
    with pytest.raises(TypeError):
        add(5, "hello")


# ! For check message about error
def test_divide_by_zero_raises_value_error_with_message():
    with pytest.raises(ValueError) as excinfo:  # excinfo - is a wrapper object containing info about the error
        divide(10, 0)

    # Check that the error text contains the required phrase
    assert "You can't divide by zero!!" in str(excinfo.value)
