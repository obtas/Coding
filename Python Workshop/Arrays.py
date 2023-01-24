# Arrays are the umbrella term for collections of data
# Lists - [] ordered, mutable
# tuples - () ordered, immutable
# dictionaries - {} unordered, mutable, key value
# sets - {} unordered, mutable, unique

animals = ["aardvark", "sloth", "aiai", "zebra"]
print(animals[2])
print(animals[-1])

animals[1] = "panda"

print(animals[1])
print("panda" in animals) # returns true if word is in list
animals.append("tiger") # adds word to end of list

animals.insert(2, "tardegrade") # adds tardegrade in second position in list
print(animals)

# lists can take in any data type
cafe_order = [12, "John Cena", True, ["latte", "carrot cake"]] # can add a list or dictionaries within a list
print(cafe_order[3][1]) # calls carrot cake

# Length of a list (how many elements)
print(len(animals))

print("-------------------------------------")

for a in animals:
    print(a) #place variable name in bracket, not the name of the array otherwise it just prints the array 6 times as there are 6 elements.

# Tuples - cannot be modified
colours = ("red", "green", "blue", "purple")
print(colours[2])

# To change a tuple, you'd have to remake it
colours = ("lilac", "silver", "gold")
print(colours)

# Dictionaries - Unordered, mutable, key: value pairs
noises = {"cow": "moo!", "duck": "quack!", "cat": "meow!"}
print(noises["cow"])

noises["chicken"] = "cluck!"
print(noises)

# Sets - unordered, unique values
fruit = {"lemon", "unique", "apple", "apple"}
print(fruit)
print("pear" in fruit) # can check if element is in the set - Boolean
