#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
first = ["spaghetti", "lasagna", "pasta carbonara"]
second = ["steak", "pork chops", "ribs"]
side = ["salad", "bread and butter", "French fries"]

#Generates a random integer.
aRandomIndex = randint(0, len(first)-1)
aRandomIndex2 = randint(0, len(second)-1)
aRandomIndex3 = randint (0, len(side)-1)

answer = input("If you would like a meal with a first course, second course, and a side, Type ok.")
if answer == "ok":
    print ("Your meal consists of", first[aRandomIndex], ",", second[aRandomIndex2], ",", "and", side[aRandomIndex3], ".")
