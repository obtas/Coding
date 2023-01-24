# For Loop is triggered x number of times
# Range python

print(range(5))
print(*range(5)) # Returning values 0,1,2,3,4
print(*range(5,10)) # 5, 6,7,8,9
print(*range(10,0,-1)) # 10,9,8,7,6 .....1, counts backwards
print(*range(5,21,2)) # Count from 5 - 20 in increments of 2

range(10)
for x in range(10):
    print(x)
print("========================")

range(11)
for number in range(11):
    print(number)