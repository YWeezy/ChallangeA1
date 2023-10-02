import intro
from Asgaard import *
from gym import *
from starkindus import *
from choices import *
from os import system
items = []

def options():
    print(items)
    print("Deadpool: So to become the most op character in the universe il have to first buff my health up.")
    print("Why not steal some Avenger things.")

    print("a) Asgaard")
    print("b) Stark industries")
    print("c) Gym")
    if "MARK DEADPOOL(Space travel)" in items:
        print("Vormir")
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
    elif choice == "d" and "MARK DEADPOOL(Space travel)" in items:
        vochoice1()

options()




# import galgje
# import memorize
# import riddle