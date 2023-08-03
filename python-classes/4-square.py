#!/usr/bin/python3
'''
This program has a class square that defines a square with a private instance attribute named size
'''
class Square:
    ''' delcaration of the class'''
    def __init__(self, size=0):
        '''defining and initializing the square object with a private size attribute'''
        self.__size = size 
    @property
    def size(self):
        '''defining the method for retrieving the size attribute'''
        return self.__size
    @size.setter
    def size(self, value):
        '''
        property setter method to set the attribute.
        Creating the loop for checking whether the size is an integer and not less than zero
        '''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        '''defining the method to compute the current squared area'''
        self.area = self.__size**2
        return self.area
    def my_print(self):
        '''the public instance method that prints in stdout the square with the character'''
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
              print("#" *self.__size)
              
