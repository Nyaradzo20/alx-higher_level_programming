#!/usr/bin/python3


class BaseGeometry:
    '''Base... class'''

    def area(self):
        '''raise exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validating value'''
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
