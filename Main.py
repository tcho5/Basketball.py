import sys
import os
import time
from Player import *
# import random
# import array

class User:
    def __init__(self):
        self.user = None
        self.pw = None

def afternoonOptions():
    print("What would you like to for your Afternoon schedule?\n")
    print("########### OPTIONS ##############")
    print("1) Check out my stats... (No Energy) How good am I?")
    print("2) Check out Upcoming Events... (No Energy) Best ways for me to show off")
    print("3) Go hit up the courts...(2 Energy) What's a better way then to socialize and play with other hommmies")
    print("4) Find a job...(1 Energy) I do need some money to buy equipments")
    print("5) Hit the gym (3 Energy)... Where I can do drills and workout. I need to have a gym membership tho ($50)")
    print("10) Save the game...")

def morningOptions():
    print("What would you like to for your morning schedule?\n")
    print("########### OPTIONS ##############")
    print("1) Check out my stats... (No Energy) How good am I?")
    print("2) Go for a morning Jog...(1 Energy) Gotta stay in top shape")
    print("3) Attend Classes...(2 Energy) Can't fail my classes")
    print("10) Save the game...")
    print("Jasmine) Cheat code coming soon...")

def game():
    days = 1
    morning = True
    valid = True
    while(days != 51):
        energy = 5
        if(morning and valid):
            space()
            print("Day " + str(days) + "\n")
            print("Energy: " + str(energy) + "\n")
            print("What a fresh new Day...")
            morningOptions()
        else:
            print("It is the afternoon...")
            afternoonOptions()
        choice = input(" Option(1-4): -> ")
        if(choice == "1"):
            print("choice 1")
            if(morning):
                morning = False
            else:
                print("It's the afternoon")
            break
        elif(choice == "2"):
            print("choice 2")
            if(morning):
                morning = False
            else:
                print("It's the afternoon")
            break
        elif(choice == "3"):
            print("choice 3")
            if(morning):
                morning = False
            else:
                print("It's the afternoon")
            break
        else:
            print("invalid choice... please try again. ")
            valid = False
            if(morning):
                morningOptions()
            else:
                afternoonOptions()
def space():
    print("\n" * 5)

def startGameText(newUser):
    print("\n" * 50)
    print("######################## Beta 1.0 ################################")
    print("You are a newbie who wants to dreams of becoming the next top prospect in the NBA")
    print("But first and foremost... What is your damn name again?\n")

    first = input("First Name: -> ")
    last = input("Last Name: -> ")
    print("Okay... You are " + first + " " + last)
    newUser.setFirst(first)
    newUser.setLast(last)
    space()
    print("The concept of this game is very simple...")
    print("You get 50 days to train yourself and make it into the NBA Draft")
    print("Each day you get several options to choose from to live on with your day")
    print("Your choices, your actions, determine how high you make it in the draft. Will you even make it...???")

    time.sleep(5)
    print("Are you ready? Doesn't matter here we go...")
    time.sleep(2)

def startMenuText():
    print("Welcome to basketballRP version 1.0!\n")
    print("Please enter a valid number option")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")

def Start():
    print("\nWe are now starting the game...\n")
    username = input("Please enter a username: ")
    newUser = Player()
    newUser.setUserName(username)
    startGameText(newUser)
    space()
    game()
    #Have a Password System and then verify if ID exist in system

def main():
    startMenuText()
    verify = False
    while (verify == False):
        command = input("User Input -> ")
        if command.lower() == "start":
            Start()
            # pass
            break
        elif command.lower() == "load":
            pass
        elif command.lower() == "exit":
            print("Until next time!")
            sys.exit()
        else:
            print("Invalid Entry... Try again!")

main()
