# File IO Input Output
# Using Python to read from files, do x with the data and modify the data in the files
# Python can be used to  change .txt, .csv, .MD

# Opening the file and storing it as variable fruit.txt
# fruit_file = open("fruit.txt")
# fruit_line = fruit_file.readline() # Reading first line of the file
# fruit_file.close()

# print(fruit_line)

# colour_file = open("colours.txt")
# colour_line = colour_file.read()
# print(colour_line)

# for line in colour_line:
#     print(line)

# line = colour_line.split(",")
# print(line)

# fruitFile = open("fruit.txt", "r") # "r" read mode, "a" append mode
# data = fruitFile.readline()
# print(data)
# fruitFile.close()

# fruitFile = open("fruit.txt", "a")
# fruitFile.write("strawberry")
# fruitFile.close()

numbersFile = open("numbers.txt", "w")
#lines = numbersFile.readlines()
#for line in lines:
for i in range(11):
    numbersFile.write(f"\n{str(i)}")
numbersFile.close()

    

