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
    print(mp.questions[0].q+"\n"+mp.questions[0].a1+"\n"+mp.questions[0].a2+"\n"+mp.questions[0].a3)

if __name__=="__main__":
  main()
