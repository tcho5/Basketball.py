import sys
import os
import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.height = 6.2
        self.fame = 25
        self.position = guard

def main():
        print("Welcome to basketballRP version 1.0!")
        print()
        print("Please enter a valid number option")
        print("1.) Start")
        print("2.) Load")
        print("3.) Exit")
        option = raw_input(" User Input -> ") ## 
        if option == "1":
            start()
        elif option == "2":
            pass
            load()
        elif option == "3":
            print("Until next time!")
            sys.exit
        else:
            main()
        
        

main()
