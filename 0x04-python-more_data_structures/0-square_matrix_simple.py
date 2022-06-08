#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
     Use:Matrix([num_of_rows, num_of_columns],
     [2D array or 1D array or None/blank])
     '''
    new_matrix = [list(map(lambda a: a ** 2, b))for b in matrix]
    '''lamba function is an anonymous function
       which works on single expressions'''
    '''
        Work with Python’s map ()
        Use map () to process and transform
       iterables without using an explicit loop
       Combine map () with functions like filter ()
       and reduce () to perform complex transformations
       Replace map () with tools like list
       comprehensions and generator expressions
     '''
    return new_matrix
