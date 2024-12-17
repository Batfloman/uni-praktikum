from enum import Enum;

class Units(Enum):
    KG = "kg"

class Unit:
    def __init__(self):
        self

    def __str__(self):
        return "\u00B7"
    
    def __add__(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Units cannot be added with other types!")
        
        # if 

    def __radd__(self, other):
        return self.__add__(other);
    
    def __pow__(self, other):
        return;