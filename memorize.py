from os import system
import time
import random
retryask = False
def mem():
    print("welcome to Memorize sequence")
    for x in range(5):

        randmin = 1000
        randmax = 9999
        if x > 1:
            randmin = 10000
            randmax = 99999

        if x > 3:
            randmin = 100000
            randmax = 999999
        
        print(f"Round " + str(x + 1))
        time.sleep(5)
        system('clear')
        number = random.randint(randmin,randmax)
        
        temp_printint(number)
        inp = int(input())
        if number == inp:
            print("correct")
        else:
            print("incorrect")
            retryask = True
            break
    if retryask == True:
        ans = input("Retry? 'yes' or 'no'")
        if ans == "yes":
            mem()
        else:
            pass


def temp_printint(val: int):
    print(val)
    time.sleep(2)
    system('clear')
mem()