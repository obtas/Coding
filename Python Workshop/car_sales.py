# From this .csv you should extract the data, convert it to a series of lists and work out the following: 
# 1)	Sum of cars sold by Ford in total
# 2)	Sum of cars sold in May 2019
# 3)	Average of cars sold in Aug 2019
# 4)	Car manufacturer who sold most cars Jan 2019 – Apr 2019
# 5)	Month where the least amount of cars were sold

# carFile = open("carSale.csv")
# carFile = carFile.readlines()
# print(carFile)

# # Looping through data and stripping unwanted stuff
# for i in carFile:
#     line = i.strip() #strip gets rid of stuff
#     #print(line)
#     line_array = line.split(",") #split converts from list to array
#     #print(line_array)
# print("==============================================")
# for data in line_array:
#     new_data = data.replace("'","")
#     print(new_data)
        
#=====================================================================================
car_data = open("carSale.csv")
car_data = car_data.readlines()

split_data = []

# Looping through our data and stripping unwanted stuff
for i in car_data:
    line = i.strip() # Getting rid of \n and stuff like that
    line_array = line.split(",") # Splitting converting strings into []
    split_data.append(line_array) # Adding the data to a new array

# Capture the data for Ford
ford_data = []
index_num = 0 
print("*******************************************")
#print(split_data[1])
for x in split_data[1]:
    if index_num > 0:
        cast_data = int(x)
        ford_data.append(cast_data)
    index_num += 1

print(ford_data)

print("================================================")
# 1)	Sum of cars sold by Ford in total

ford_sum = print(sum(ford_data))
print(f"the total number of cars sold by Ford is {ford_sum}")

