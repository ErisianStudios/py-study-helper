import random
from flashcards import Ports
from flashcards import MultipleChoice as mp



def main():
    qa = random.randrange(0,2)
    if qa == 0:
        show_ports()
    elif qa == 1:
        show_multiple_choice()
    else:
        print("DEBUG: qa out of range")
    main()

def show_ports():
    rnd = random.randrange(0,len(Ports.q)) 
    print(Ports.q[rnd])
    answer = input("Answer: ")
    if answer.lower() == Ports.a[rnd].lower():
        print("Correct!")
    elif answer.lower() == "quit":
        quit()
    else:
        print("Incorrect. The answer is: " + Ports.a[rnd])

def show_multiple_choice():
    i=random.randrange(0,len(mp.questions))
    print(mp.questions[0].q+"\nA)"+mp.questions[0].a1+"\nB)"+mp.questions[0].a2+"\nC)"+mp.questions[0].a3)
    answer = input("Answer: ")
    if answer.lower() == mp.questions[0].ca:
        print("Correct!")
    elif answer.lower() == "quit":
        quit()
    else:
        print("Incorrect! The answer is: " + mp.questions[0].ca)

if __name__=="__main__":
  main()
