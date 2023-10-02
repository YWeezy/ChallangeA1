from os import system
import time

def quizz():

    quiz = ["What is the first MCU movie?",
            "Which superhero, known for his red suit and acrobatic skills, is often referred to as the Merc with a Mouth?",
            "What is the strongest alloy called?",
            "How many infinity stones are there?",
            "What is the superhero team called that works under S.H.I.E.L.D?"]

    answers = ["iron man", "deadpool", "vibranium", "6", "the avengers"]

    def qui():
        system('clear')
        print("Welcome to the quiz")
        print("Answer the quiz in lowercase!")


        for ind, question in enumerate(quiz):
            while True:  # Continue until the user provides the correct answer
                print(question)
                inp = input()

                if inp == answers[ind]:
                    print("Correct!")
                    time.sleep(2)
                    system('clear')
                    break  # Exit the loop if the answer is correct
                else:
                    print("Incorrect. Try again.")

    qui()

