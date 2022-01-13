import random
import sys



gameRunner =1
while gameRunner:
    sysNum = random.randint(1, 9)
    try:
        userInput = int(input("Input number between 1-9: "))
        if userInput >9 or userInput<1:
            print("Number should be within 1-9")
        elif userInput == sysNum :
            print(f"Well guessed! : {userInput}")
            gameRunner=0
        else:
            print(f'Incorrect Guess system Guess : {sysNum} but you said : {userInput}')

    except: print("Incorrect Input, try again !");