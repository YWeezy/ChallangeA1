from riddle import *
import time
from os import system




def aschoice1():
    system('clear')
    print("Asgaard entrance...")
    print("Guard: Welcome to Asgaard. What is your porpuse?")
    print("a) Kill him")
    print("b) I want to see Thor")
    print("c) Is that a dog?")
    choice = input("write in lower caps")

    if choice == "a":
        print("You got a speared through the stomach.")
        time.sleep(2)
        system('clear')
        aschoice1()
    elif choice == "b":
        print("Guard: Since you asked so nicely. Sure.")
        system('clear')
        time.sleep(2)
        return aschoice2()
    elif choice == "c":
        print("you got used as a bone")
        time.sleep(2)
        system('clear')
        aschoice1()

def aschoice2():
    print("Thor's room...")
    
    print("a) Ask him the hammer")
    print("b) Try to kill him")
    choice = input("write in lower caps")

    if choice == "a":
        riddlep = False
        print("Deadpool: can i have your hammer?")
        print("Thor: no your not worthy.")
        print("Deadpool: why not i have a high IQ. Im loy..")
        print("You have a high IQ. Fix these riddles and you can have it.")
        time.sleep(4)
        while riddlep == False:
            riddlep = ridd()
            if riddlep == True:
                print("Yesss lets, get out of here")
                itemr = "mjolnir"
                return itemr
            else:
                print("try again")
                
        
    elif choice == "b":
        
        print("He put the hammer on top of you and you couldn't move.")
        time.sleep(2)
        system('clear')
        aschoice2()
