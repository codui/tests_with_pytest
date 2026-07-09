from src.calculator import add


def test_add():
    # Using assert to check
    assert add(2, 3) == 5


# ! Failed test for example
def test_add_with_wrong_expectation():
    """This test is specifically designed to fail."""
    # Call a function directly inside an assert to see the error details
    assert add(2, 2) == 5
