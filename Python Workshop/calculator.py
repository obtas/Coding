calc=["1.Add", "2.Subtract", "3.Multiply", "4.Divide", "5.Power"]

print(*calc, sep="\n")
command=input("What would you like to do: ")

print(command)

x = int(input("Choose a number between 1-5: "))
if x > 5:
    print("Choose a number between 1-5")

y = int(input("Choose another number between 1-5: "))
if y > 5:
    print("Choose a number between 1-5")

if command == "Add":
    print(x + y)
elif command == "Subtract":
    print(x - y)
elif command == "Multiply":
    print(x * y)
elif command == "Divide":
    print (x / y)
elif command == "Power":
    print (x**y)
else:
    print("Error: Command not found")
