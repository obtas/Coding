# Class for cake
# Class - Recipe, blueprint for what we want our objects to be

# Class is a default function called a constructor that we can use to make objects

# class cake:
#     frosting = True
#     flavour = "choc"
#     size = 15
    
#     def bake(self):
#         return "In the oven now!"
    
# cake1 = cake()

# print(cake1) 
# print(cake1.frosting) # Object Frosting - True
# print(cake.frosting) # Class Frosting - True

# print(cake1.bake())

#-----------------------------------------------------

class penguin:
    
    # You specify attributes and what data type they are
    # Constructor - function that takes in params and sets the attributes of our created object
    # __init__ - the initialising function that runs when the object starts
    
    def __init__(self, name, fish_eaten, dancing):
        self.name = name
        self.fish_eating = fish_eaten
        self.dancing = dancing
        
        # Setting the values of our object based on whats entered
        
    def swim(self):
        return "Swimming quickly!"
    
    def swim2(self):
        return f"{self.fish_eating} fish .... swimming to get more"
    
    def __str__(self):
        return f"name: {self.name} fish eaten: {self.fish_eating} and dancing: {self.dancing}"
    
penguin1 = penguin("Pingu", 25, True)
    
print(penguin1.swim())

print(penguin1)
