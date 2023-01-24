#Iteration - Repeating a block of code to save time and development

#while loop
# while loop run a block of code until a condition is no longer true
import random

counter = 0
while counter <= 100:
    print (f"Value of counter is {counter}")
    # assigning counter to a new value which is old value +1
    # counter = counter + 1
    counter +=10
    
    if counter == 50:
        print("Hit value 50 exactly")
        break
    
#counter = 1
#while counter < 100:
    #print (f"Value of counter is {counter}")
    # assigning counter to a new value which is old value +1
    # counter = counter + 1
    #counter += random.randint(2,15)
