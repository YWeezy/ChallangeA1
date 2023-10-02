import time
from os import system
from galgje import *
lijst = ["pepper","playboy","billionare"]

def strchoice2():
    system('clear')
    print("mark room...")
    print("Deadpool: What to do?")
    print("a) Touch everything")
    print("b) Dance")
    print("c) Walk further")
    
    
    choice = input()
    time.sleep(2)
    
    
    print("Deadpool: now lets pick a suit")
    time.sleep(2)
    print("INTRUDER!!!!!")
    print("(claws pick up deadpool)")
    print("JARVIS: Who might You be??")
    print("Deadpool: Im tony the alternate version")
    print("JARVIS: BEGIN VERIFICATION")
    time.sleep(6)
    system("clear")
    print("JARVIS: Welkom bij galgje (tony related) MADE BY DUTCH DEVELOPERS")
    return gal(lijst)

def strchoice1():
    system('clear')
    print("Stark Industries entrance...")
    print("Receptionist Woman: Can i help you")
    print("a) You never change do you, darling?")
    print("b) Im the janitor")
    print("c) Kill her")
    choice = input()

    if choice == "a":
        print("Receptionist Woman: And who are you supposed to be")
        print("Deadpool: I'm Tony Stark. And I've saved my best weapon for you.")
        print("Deadpool: This mask is confidential. Now if you excuse me (walks by)")
        
        time.sleep(8)
        system('clear')
        return strchoice2()
    elif choice == "b":
        print("Receptionist Woman: We dont have any janitors")
        print("Deadpool: no hablo ingles")
        print("Receptionist Woman: Get out!!")
        
        time.sleep(4)
        system('clear')
        strchoice1()
    elif choice == "c":
        print("I cant kill girls")
        
        time.sleep(3)
        system('clear')
        strchoice1()

