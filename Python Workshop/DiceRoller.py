import random

# def rollSix():
#     return random.randint(1, 6)

# rollSix()
# print(rollSix())

# print("-----------------------------------")
# def rollEight():
#     return random.randint(1, 8)

# # rollEight()
# print(rollEight())

# print("-----------------------------------")
# def rollTen():
#     return random.randint(1, 10)

# rollTen()
# print(rollTen())
# print("-----------------------------------")

# roll = []

# def rollSix4():
#     print("run")
#     return random.randint(1, 6)
 
# print(rollSix4())

# print("-----------------------------------")

def rollDice(num):

    all_dice = []

    for roll in range(5):
        roll = random.randint(1, num)
        all_dice.append(roll)
    print(all_dice)
    
    lowest = min(all_dice)
    all_dice.remove(lowest)
    total = sum(all_dice)
    print(total)
    return all_dice
    
#rollDice(6)
print(rollDice(6))