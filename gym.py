import time
from os import system




def gychoice1():
    system('clear')
    print("Gym...")
    print("Captain America is sparing a dummy")
    print("a) Kill him and take his shield")
    print("b) Talk to him")
    choice = input()

    if choice == "a":
        print("You backstabbed him and took his shield")
        print("Deadpool: That was easy")
        
        time.sleep(5)
        system('clear')
        return "Shield"
    elif choice == "b":
        print("You talked for ever and died of old age")
        system('clear')
        time.sleep(3)
        gychoice1()
    