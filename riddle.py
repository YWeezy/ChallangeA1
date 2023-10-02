from os import system
import time
riddles = ["What gets bigger the more you take away?", "What gets wet while drying?", "David’s parents have three sons: Snap, Crackle, and what’s the name of the third son?", "I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?"]
answers = ["hole", "towel", "david", "shadow"]

def ridd():
    system('clear')
    done = True
    print ("Welcome to riddles")
    print ("Answer the riddles in low caps and one word !!")
    for ind, x in enumerate(riddles):
        print(x)
        inp = input()
        
        if inp == answers[ind]:
            print("correct")
            time.sleep(2)
            
        else:
            print("incorrect")
            time.sleep(2)
            done = False
            break
        
    if done == True:
        return True
    else:
        return False
        

      
