"""
an empty class
"""
class BaseGeometry:
    """
    empy class
    """
    pass

    """
    a function that defines area and raise exception
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
