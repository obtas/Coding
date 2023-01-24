from abc import ABC, abstractmethod

class human(ABC):
    
    @abstractmethod
    def breathe(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
class woman:
    def __init__(self, height, race, style):
        
        self.height = height
        self.race = race
        self.style = style
        
    def breathe(self):
        return "breathe gentle"
    
    def __str__(self):
        return f"I am {self.height} cm tall, I am {self.race} and my style is {self.style}"
    
woman1 = woman(165, "black", "basic")

print(woman1.breathe())
print(woman1)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# fav_colour = input("Enter your favourite colour: ")
# password = input("Enter your password: ")

class user:  
        
    _name = "satta"
    _age = 27
    _fav_colour = "purple"
    _password = 1234
    _name2 = ""
    
    def displayName(self, password):
        if password == self._password:
            return f"Your name is {self.name}"
        else:
            return "Enter the correct password" 
        
    def displayAge(self, password):
        if password == self._password:
            return f"Your age is {self._age}"
        else:
            return "Enter the correct password"  
        
    def displayName(self, password):
        if password == self._password:
            return f"Your name is {self._name}"
        else:
            return "Enter the correct password"       
        
    def displayUser(self, password):
        if password == self._password:
            return f"Your name is {self.name}, you are {self.age} years old and your favourite colour is {self.fav_colour}"
        else:
            return "Enter the correct password"
        
    def setName(self, password):
        if password == self._password:
           name2 = input("Enter your new name: ")
           _name2 = _name2 + name2 
           return f"Your new name is {self._name2}"
        else:
           return "Enter the correct password"
        
user1 = user()
        
print(user1.displayName(1234))
print(user1.displayName(2345))
print(user1.displayAge(1234))
print(user1.setName(1234))
        
