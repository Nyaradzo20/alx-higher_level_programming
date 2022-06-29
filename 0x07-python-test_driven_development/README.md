Test Driven Development (TDD) is an evolutionary approach to building and designing software solutions. It is consisting of small cycles in which we are writing a unit test, that will initially fail, and then implementing the minimum amount of code to pass that test. After that code can be refactored to follow some good principles. Refactoring has a safety net, because we wrote the tests already, so we can reshape our solution stress-free.

These three important steps of TDD are easy to remember by using something that I like to call the TDD mantra. It goes like this: t really have a color for that one. So there you go, TDD Mantra Red
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
You might wonder what is the difference between just writing unit tests for your code and TDD? In general, we are using unit tests in both cases. The crucial difference between TDD and traditional testing is the moment in which we are writing the tests. When we are writing code using TDD we first write the tests and then the code itself, and not another way around. The benefit of this approach is that we are minimizing the possibility of forgetting to write tests for some part of the code. Ideally, we end up with the code that is fully tested upfront and solutions that are implemented using TDD usually have 90%-100% of code covered with tests.

Of course, when our code is tested it is less likely that we have a bug in our system. Another important difference is that we are writing small chunks of code to satisfy our test. This way the process itself drives our design and forces us to keep things simple. By using TDD we avoid creating over complicated designs and overengineered systems. Arguably this is the biggest benefit of this approach. When we use it we end up with clearer design and API. This approach also forces you to design classes properly and to follow good code principles like SOLID and DRY. Personally, I find this way of development as a great procrastination killer and a great motivator. It kinda keeps you in the zone 
****************************************************************************************************************TASKS 
0. Integers addition
mandatory
Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module.

2.rite a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any moDULE
 2.Write a function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
You are not allowed to import any module

3.Write a function that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer
You are not allowed to import any module

4.Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module
5.Since the beginning you have been Interactive . For this exercise, you will add Unittests.

6..In this task, you will write unittests for the function def max_integer(list=[]):.

Your test file should be inside a folder tests
You have to use the unittest module
Your test file should be python files (extension: .py)
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the function below
We strongly encourage you to work together on test cases, so that you t miss any edge creating  Write a function that multiplies 2 matrices:

Read: Matrix multiplication - only Matrix product (two matrices)

Prototype: def matrix_mul(m_a, m_b):

m_a and m_b must be validated with these requirements in this order

m_a and m_b must be an list of lists of integers or floats:

if m_a or m_b is not a list: raise a TypeError exception with the message m_a must be a list or m_b must be a list
if m_a or m_b is not a list of lists: raise a TypeError exception with the message m_a must be a list of lists or m_b must be a list of lists
if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or m_b can't be empty
if one element of those list of lists is not an integer or a float: raise a TypeError exception with the message m_a should contain only integers or floats or m_b should contain only integers or floats
if m_a or m_b is not a rectangle ( should be of the same size): raise a TypeError exception with the message each row of m_a must be of the same size or each row of m_b must be of the same size
If m_a and m_b t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied

You are not allowed to import any module

7.Write a function that multiplies 2 matrices by using the module NumPy

To install it: pip3 install numpy==1.15.0

Prototype: def lazy_matrix_mul(m_a, m_b):
Test cases should be the same as 100-matrix_mul but with new exception type/message
8.Create a function that prints Python strings.

Prototype: void print_python_string(PyObject *p);
Format: see example
If p is not a valid string, print an error message (see example)
Read: Unicode HOWTO
About:

Python version: 3.4
You are allowed to use the C standard library
Your shared library will be compiled with this command line: gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
