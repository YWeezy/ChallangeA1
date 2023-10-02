import time
import os
from rekenen import*
from quiz import*

def clear_screen():
    os.system('clear')

def gychoice1():
    clear_screen()
    
    print("Vormir...")
    print("The desolate world, a passage way that demanded the ultimate sacrifice.")
    print("a) Sacrifice: chimichangas")
    print("b) Sacrifice: your dignity")
    print("c) Sacrifice: your fast healing")
    
    choice = input().strip().lower()

    if choice == "a":
        print("Not eating chimichangas made you eventually insane....")
        time.sleep(5)
        print("But you managed.")
        time.sleep(5)
        clear_screen()
        return "passage"

    elif choice == "b":
        print("You made a personal sacrifice and retained your dignity.")
        time.sleep(3)
        print("However, you did not gain passage")
        time.sleep(3)

    elif choice == "c":
        print("You wouldn't be able to control the power after you lost your fast healing.")
        time.sleep(3)
        print("you gave up.")
        time.sleep(3)
        clear_screen()
        gychoice1()

# Example usage:
result = gychoice1()
if result == "passage":
    print("You were granted passage!")
else:
    print("Your cosmic quest continues...")

print('after that difficult task you used the passage to go to the The Quantum Realm...')
clear_screen()

print('''As Deadpool collected each artifact, he unknowingly drew the attention of a cosmic menace known as thanos 
This formidable entity sought to wield the combined power of the infinity stones to reshape the universe in its own image.
In a climactic battle at the edge of reality, Deadpool faced off against thanos, armed with the artifacts he had collected. 
With his unorthodox fighting style and a quip for every occasion.''')
clear_screen()
    
print("deadpool: Those stones belong to me, and i will use force if nessesary.")
print("Thanos: alright let's play a game for them")

reken()
clear_screen()

print('thanos: you cheater')
print('deadpool: you are just a sore loser')
print('thanos: lets do another game')

quizz()

