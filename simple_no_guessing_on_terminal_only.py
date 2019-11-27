"""
Created on Wed Nov 27 15:49:32 2019

@author: pranav
"""
from random import shuffle
from random import randint

answer = randint(0,20)
guessed_no = int(input("Guess an integral number.: "))
i = 1
while answer != guessed_no:
    if guessed_no > 20 or guessed_no < 0:
        print("Sorry, the no. is out of bounds!")
        guessed_no = int(input("Keep guessing: "))
        i = i+1
        continue
    else:
        if guessed_no in range(answer-3,answer+4):
            print("You are close..")
            guessed_no = int(input("Keep guessing: "))
            i = i+1
            continue
        else:
            print("Nah! It's a bit far away...")
            guessed_no = int(input("Keep guessing: "))
            i = i+1
            continue
        break
else:
    print("Horrayyyy! The guess is right and the no. is {}. It took you {} guess(s) to get to the correct answer.".format(answer,i))