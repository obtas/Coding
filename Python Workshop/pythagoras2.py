command = input("Which side do you want to calculate: ")

if command == "a":
    b=int(input("Enter the length of side b: "))
    c=int(input("Enter the length of side c: "))
    bsq=b**2
    csq=c**2
    asq= csq - bsq
    a = asq ** 0.5
    print("the length of side a is {a}".format (a=a))
if command == "b":
    a=int(input("Enter the length of side a: "))
    c=int(input("Enter the length of side c: "))
    asq=a**2
    csq=c**2
    bsq= csq - asq
    b = bsq ** 0.5
    print("the length of side a is {b}".format (b=b))
if command == "c":
    a=int(input("Enter the length of side a: "))
    b=int(input("Enter the length of side b: "))
    asq=a**2
    bsq=b**2
    csq= asq + bsq
    c = csq ** 0.5
    print("the length of side a is {c}".format (c=c))