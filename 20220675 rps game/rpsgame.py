#simple game of rock,paper,scissors with if,else and while loop
import random


bot_score=0
your_score=0

print("let's start the game(IF YOU WANT TO QUITE THAN JUST ENTER THE'QUITE')")

while True:
    #choices for bot to choose among this
    choices=["rock", "paper", "scissor"]
    a=input("enter your choice ROCK,PAPER OR SCISSOR :")
    bot=random.choice(choices)
    #main program of this game 
    #conditons of win and loose
    if a==bot:
        print("it's a tie")
        if a=="rock":
            if bot=="paper":
               print("you lose because bot choose ",bot)
               bot_score+=1
        else:
            print("you win because bot choose ",bot)
            your_score+=1
    elif a=="paper":
        if bot=="scissor":
            print("you lose because bot choose ",bot)
            bot_score+=1
        else:
            print("you win because bot choose ",bot)
            your_score+=1
    elif a=="scissor":
        if bot=="rock":
            print("you lose because bot choose ",bot)
            bot_score+=1
        else:
            print("you win because bot choose ",bot)
            your_score+=1
    elif a=="quite":
        print("sure")
        break

print("final scores are")
print("your score is",your_score)
print("bot score is",bot_score)

if your_score>bot_score:
    print("CONGRATULATIONS! YOU WIN THE GAME")
else:print("SORRY! you lose the game ")
#This simple programme tought me lot of about python basics
#like when and how to use while loop ,if else statement and many things
#by continue this program I get to know that python is esier than other language for learning
#I learn loop on Linkdin and some help of tutors.
