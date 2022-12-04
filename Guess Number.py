#Guess The Number !!
print("Welcome to Guess the Number (⁠ ⁠╹ ⁠▽⁠ ╹⁠ ⁠) !!")

lower=int(input("Enter lower range: "))
upper=int(input("Enter upper range: "))

import random 
score=0
print()
while(True):
    radnum=random.randrange(lower,upper)
    trys=0
    while(True):
        guess=int(input("Guess: "))
        if (guess==radnum):
            print("You Guessed it right!")
            score=score+1
            break
        else:
            if(guess>radnum):
                print("Your Guess was High")
                trys=trys+1
            else:
                print("Your Guess was Low")
                trys=trys+1
            print("Trys left:{}\n".format(3-trys))
        if(trys>=3):
            print("Sorry you had your Chance :(")
            break
    print("Number was",guess)
    print("Your score is",score)
    PA=input("\nWanna Try Again (y / n) : ")
    PA=PA.lower()
    if (PA=='y'):
        continue
    elif(PA=='n'):
        break
    else:
        print("Uhm yes(y) or no(n) ?\nAnyways,")
        break
print("It was Fun playing with you!")