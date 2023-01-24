ages =[
    12,18,33,84,45,67,12,82,95,16,10,23,
    43,29,40,34,30,16,44,69,70,74,38,65,
    36,83,50,11,79,64,78,37,3,8,68,22,4,
    60,33,82,45,23,5,18,28,99,17,81,14,88,
    50,19,59,7,44,93,35,72,25,63,11,69,11,
    76,10,60,30,14,21,82,47,6,21,88,46,78,
    92,48,36,28,51]

length = len(ages)

print(length)
print("-----------------------")
for age in ages:
    print(age)
print("-----------------------")
for x in ages:
    x += 1
    print(x)
print("-----------------------")
people = [
    18,33,45,16,23,
    43,29,40,34,30,16,44,38,65,
    36,50,64,37,22,
    60,33,45,23,18,28,17,
    50,19,59,44,35,25,63,
    60,30,21,47,21,46,48,36,28,51] 
print(people)
for x in people:
    if x > 65 and x < 16:
        print("you did your list wrong")
else:
    print("your list looks goodt")
print("------------------------")
print(len(people))
print("------------------------")
people.sort()
print(people)
print("------------------------")
prop = (43 / 81) * 100
print(prop)
print("-------------------------")
new_ages = []
for age in ages:
    if age > 16 and age < 65:
       new_ages.append(age)
print(new_ages)
    