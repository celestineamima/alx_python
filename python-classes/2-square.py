#!usr/bin/python3
"""module with a class that defines a square"""
class Square:
    """defining square object
    args:
    size(param
    ) is assumed to be an int"""
    def __init__(self, size=0):
            self.__size = size 
            """private attribute"""
            while type(size) is int:
                  if size < 0:
                        raise ValueError("size must be >= 0")
                  break
            else:           
                raise TypeError("size must be an integer")
    """public instance method takes parameter self and can be accessed both inside and outside class"""
    def area(self):
          """area"""
          return self.__size ** 2
          
         
