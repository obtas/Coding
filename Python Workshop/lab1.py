print("Hello World")

print("Del Toro's Pinocchio")
print("Knives Out: Glass Onion")
print("Jojo's Bizarre Adventure")

name = input("Please enter your name: ")
print("Hello " + name)

drink = input("What drink would you like? ")
print(drink + " is coming right up! Please wait...")

whipcream = bool(input("Would you like whipped cream?"))

quantity = int(input("How many drinks would you like?"))

print("ok {name} Here is your {quantity} {drink}, you asked for {whipcream}.".format(name=name, drink=drink, quantity=quantity, whipcream=whipcream))

