numbers = [12,234,45,674,78,345,75,78,32,345,12,3454345, -3, 5.418412]

print(numbers)

# Prints minimum and maximum 
print(min(numbers))
print(max(numbers))

# Converts negative to positive
print(abs(numbers[-1]))

# Two to the power of 3
print(pow(2,3))

# Round numbers to decimal points
print(round(numbers[-1]))
print(round(numbers[-1], 2))

# String formatting
str = "hElLo WOrlD"
print(str.lower())
print(str.upper())
print(str.title()) # Hello World
print(str.replace("l", "z")) # Replaces all small l's with z's
print(str.lower().replace("l", "z")) # Replaces all l's (l/L) with z's

cities = "london,cardiff,newport,glasgow,leeds,birmingham"
citylist = cities.split(",")
print(citylist)

for city in citylist:
    print(city)
    
# String formatting

drink= "mocha"
size= "large"
extras = "whipped cream"

order = "{} ordered at size {} with {} added".format(drink, size, extras)

print(order)

str1 = "Hello Future"
print(str1.center(30,"*"))