import random
import os
from flashcards import Ports
from flashcards import MultipleChoice as mp

ports: bool = False
mcq: bool = False
qa: int = 0


def main():
    question_time()    

def question_time():
    clear_console()
    qa = random.randrange(0,2)
    if qa == 0:
        show_ports()
    elif qa == 1:
        show_multiple_choice()
    else:
        print("Nope.")
        wait = input("")
    question_time()

def clear_console():
    command = "clear"
    if os.name in ('nt','dos'):
        command="cls"
    os.system(command)

def show_ports():
    rnd = random.randrange(0,len(Ports.q)) 
    print(Ports.q[rnd])
    answer = input("Answer: ")
    if answer.lower() == Ports.a[rnd].lower():
        print("Correct!")
        wait=input("")
    elif answer.lower() == "quit":
        quit()
    else:
        print("Incorrect. The answer is: " + Ports.a[rnd])
        wait=input("")

def show_multiple_choice():
    i=random.randrange(0,len(mp.questions))
    print(mp.questions[i].q+"\nA) "+mp.questions[i].a1+"\nB) "+mp.questions[i].a2+"\nC) "+mp.questions[i].a3 + "\nD) "+mp.questions[i].a4+"\nE) " + mp.questions[i].a5)
    answer = input("Answer: ")
    if answer.lower() == mp.questions[i].ca:
        print("Correct!")
        wait=input("")
    elif answer.lower() == "quit":
        quit()
    else:
        print("Incorrect! The answer is: " + mp.questions[i].ca)
        wait=input("")

if __name__=="__main__":
  main()
