from Asgaard import *
from gym import *
from starkindus import *
from os import system
items = []

def options():
    print(items)
    print("Deadpool: So to become the most op character in the universe il have to first buff my health up.")
    print("Why not steal some Avenger things.")
    print("a) Asgaard")
    print("b) Stark industries")
    print("c) Gym")
    choice = input("Where you wanna go now?")

    if choice == "a":
        item = aschoice1()
        items.append(item)
        options()
    elif choice == "b":
        items.append(strchoice1())
        options()
    elif choice == "c":
        items.append(gychoice1())
        options()

options()




# import galgje
# import memorize
# import riddle