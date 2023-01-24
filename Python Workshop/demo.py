print('Hello')
print('periodt')

# Numbers
tiers = 2 # integer (int)
price = 8.99 # float

# Strings
flavour = 'Black forest'
customer = 'Satta'
message = "print('Hello')"

# Booleans
decorated = False
frosting = True

# Arrays
decorations = ['candles', 'frosting', 'sprinkles']

print(customer)
print(tiers)
print(decorations[1])
print(decorations[-1])

# naming conventions
best_practice = 'lower case and _'
camelCase = 'lowercase and Upper'
badpracticenameconvention = "Don't do this"
# print = "A4 paper, don't do this"
# percentage% = 30 - don't do this

# Inputs always takes in strings
fav_colour = input ("Please enter favourite colour: ")
print(fav_colour)

fav_num = input("Please tell me your favourite number: ")
print(fav_num)
# prints as a string

fav_num2 = int(input('Please enter your favourite number:'))
print(fav_num2)
# prints as a int

print(fav_num2 + 5)

drink_name= "John"
drink_order= "Flat white"
whipcream = bool(input('Do you want whipped cream?'))
quantity = int("2")

order = f"Name:{drink_name}, type: {drink_order}, whipped cream: {whipcream}, quantity: {quantity}"
print(order)