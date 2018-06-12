import sys
import os
#import time
#import random
##import array

class Menu:
    def __init__(self, user):
        self.user = user

class Playerr:
    def __init__(self, name):
        self.name = name
    
def Start():
    print("\nWe are now starting the game...\n")
    
    

def main():
        print("Welcome to basketballRP version 1.0!\n")
        print("Please enter a valid number option")
        print("1.) Start")
        print("2.) Load")
        print("3.) Exit")
        verify = False
        while(verify == False):
            command = input("User Input -> ")
            if command == "Start":
                Start()
                break
                #pass
   #            start()
            elif command == "Load":
                pass
            #load()
            elif command == "Exit":
                print("Until next time!")
                break
 ##               sys.exit
            else:
                print("Invalid Entry... Try again!")
                ##break

        
            
main()
