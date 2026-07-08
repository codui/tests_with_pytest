# Pytest для Python-разработчиков: Уверенное автоматизированное тестирование

## [https://stepik.org/course/259625/promo](https://stepik.org/course/259625/promo) (will open in the same tab)

To install Pytest run command in terminal:<br>
pip install pytest<br>

**Project structure:**<br>
<br>
your_root_dir/  **<-- To run the tests, you need to be here in terminal**<br>
├── src/<br>
├── tests/<br>
├── .venv/<br>
└── requirements.txt<br>
<br>
<br>

## Installing Pytest. File, Function, and Class Naming Rules. The "AAA" Pattern. Running Tests<br>
With the virtual environment activated, enter the following in the terminal:<br>
pip install pytest<br>
<br>
To check the correct installation, run the command in the terminal:<br>
pytest --version<br>
<br>
The test file must start with the prefix test_ OR end with the suffix _test.py<br>
test_calculator.py (the most common and recommended option)<br>
or<br>
calculator_test.py<br>
<br>
Within these files, each function that is a test must begin with the test_ prefix.<br>
def test_addition():<br>
<br>
A class with tests must start with the Test prefix.<br>
Methods within this class must follow the rule for functions (start with test_).<br>
>   class TestCalculator:<br>
>        def test_addition(self):<br>
>            ...<br>
>        def test_subtraction(self):<br>
>            ...<br>
<br>
All project files are located in the src folder.<br>
All test files are located in the tests folder.<br>
<br>
<br>
Project files | Corresponding test files<br>
--------------------------------------------------<br>
 calculator.py |  test_calculator.py <br>
               |<br>
               |<br>
               |<br>
               |<br>
               |<br>
<br>
<br>
The Arrange-Act-Assert pattern is used in testing.<br>
An example to understand the "Arrange-Act-Assert" pattern.<br>
    def add(a, b):
        """
        Эта функция принимает два числа и возвращает их сумму.
        """
        return a + b
<br>
Arrange: Prepare the data. In this case, these are the numbers 2 and 3 and the expected result is 5.<br>
Act: We execute the code under test. This is a call to add(2, 3).<br>
Assert: We compare the actual result with the expected result. This is the entire line with assert.<br>
<br>
<br>
To run tests, you need to run the pytest command in the terminal in the project's root folder.<br>
That is, you need to run it from the folder containing the src and tests directories.<br>
For example:
    pytest<br>
or<br>
    pytest -v (for a more visual output)<br>
<br>

## Assert syntax
assert <expression><br>
<br>
Python evaluates <expression>.<br>
If the result is True, nothing happens, and code execution continues.<br>
If the result is False, assert immediately stops execution and<br>
raises a special exception, AssertionError.<br>

<p>
When a function receives invalid data, it should not:
<ul>
<li>Silently fail: Simply exit without explanation.</li>

<li>Return a strange value: For example, None, -1, or an empty string. This is very dangerous because the error won't be noticed immediately, but will surface much later in another part of the program, making it extremely difficult to find its source.</li>

<li>Do something unpredictable.</li>
</ul>
A well-written, reliable function should report a problem immediately. It should raise an exception.
</p>
