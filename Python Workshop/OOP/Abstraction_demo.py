# Abstraction - Abstract, non physical conceptual model
# Classes and objects, objects are 'physical'
# Abstract classes, which are classes we cannot create object from

# Abstract class is more of a plan / concept of a different class

from abc import ABC, abstractmethod

# Abstract classes - they are used to plan regular classes
# import ABC from the abc package, ABC - Abstract Base Class

class animal(ABC):
    # There's no need to have a constructor ... as we can't create an animal
    
    @abstractmethod
    # defining an empty function that has no body (functionality)
    def breathe(self):
        pass
    

# Regular class
class lizard:
    
    def __init__(self, colour, legs, tail):
        
        self.colour = colour
        self.legs = legs
        self.tail = tail
        
    def breathe(self):
        return "*gentle lizard breathing*"
        
lizard1 = lizard("beige, golden", 4, True)

print(lizard1.breathe())

