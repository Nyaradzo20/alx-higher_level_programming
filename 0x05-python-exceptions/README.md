The differerence between errors and expections is ::: errors can be handled.
Errors are the problems in a program due to which the program will stop the execution .
exeptions ::e raised when some internal events occur which changes the normal flow of the program. 
 Python exceptions can be handled at the run time. An error can be asyntax (parsing) error, while there can be many types of exceptions that could occur during the execution and are not unconditionally inoperable.

::python exceptions:::
An exception (or exceptional event) is a problem that arises during the execution of a program. When an Exception occurs the normal flow of the program is disrupted and the program/Application terminates abnormally, which is not recommended, therefore, these exceptions are to be handled.
An exception is a Python object that represents an error. When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits. If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block.
:::exception handling ::
The critical operation which can raise an exception is placed inside the try clause. The code that handles the exceptions is written in the except clause.
If no exception occurs, the except block is skipped and normal flow continues(for last value). But if any exception occurs, it is caught by the except block (first and second values).
A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs.
In some situations, you might want to run a certain block of code if the code block inside try ran without any errors. For these cases, you can use the optional else keyword with the try statement.

:::built-in exceptions:::
user code can raise built-in exceptions. This can be used to test an exception handler or to report an error condition ``just like'' the situation in which the interpreter raises the same exception; but beware that there is nothing to prevent user code from raising an inappropriate error.
