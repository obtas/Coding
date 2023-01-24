grade = int(input("Please put in your grade mark: "))

if grade < 50:
    print("Fail")
elif grade >= 50 and grade < 60:
    print("Pass")
elif grade >= 60 and grade <= 70:
    print("Merit")
elif grade <= 0 or grade > 100:
    print("Error: re-enter your grade")
else:
    print("Distinction")
    
level = int(input("What Level did you study at?"))
grade2 = int(input("Please put in your grade mark: "))

if level == 1:
    if grade2 < 50:
       print("Fail")
    elif grade2 >= 50 and grade2 < 60:
       print("Pass")
    elif grade2 >= 60 and grade2 <= 70:
       print("Merit")
    elif grade2 <= 0 or grade2 > 100:
       print("Error: re-enter your grade")
    else:
       print("Distinction")
       
if level == 2:
    if grade2 < 40:
       print("Fail")
    elif grade2 >= 40 and grade2 < 50:
       print("Pass")
    elif grade2 >= 50 and grade2 <= 65:
       print("Merit")
    elif grade2 <= 0 or grade2 > 100:
       print("Error: re-enter your grade")
    else:
       print("Distinction")