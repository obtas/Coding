""" Module String for Bad Code"""

import random

DICE_ROLLER_NUMBER = 6

def roll_lots_of_dice():
    """ rolls lots of dice"""
    return random.randint(1,6)
print(roll_lots_of_dice())

def roll_lots_of_dice2():
    """ rolls lots of dice 2"""
    return random.randint(1,10)

def roll_custom_numbers(numberone, numbertwo):
    """ rolls custom numbers"""
    importantvariable = "hello"
    print(importantvariable)
    return random.randint(numberone, numbertwo)

def checkrolls():
    """ checks rolls """
    if roll_lots_of_dice2() >= 6:
        return "big number!!!"
    return "other return.."

CHECK_ROLLS_VAR = checkrolls()
print(CHECK_ROLLS_VAR)

LONG_VAR_NAME = "Unnecessary Text"
