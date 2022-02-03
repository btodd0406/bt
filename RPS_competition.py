# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:24:27 2022

@author: Brandon Todd
"""

import random
import sys

def instructions():
    print("\tHELLO AND WELCOME TO BRANDON'S ROCK PAPER SCISSORS GAME!!!")
    print("\t\t\t\t\t\t\tINSTRUCTIONS: \n\t\t\t\tChoose between ROCK PAPER AND SCISSORS")
    print("\nGAME RULES:")
    print("\tSCISSORS beats PAPER")
    print("\tPAPER beats ROCK")
    print("\tROCK beats SCISSORS")
    print("------------------------------------------------------------------")

def play():
    user = input("Make your choice: 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()
    
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        print("You and computer have both chosen {}. It's a tie.".format(computer))
    
    if is_win(user, computer):
         print("You have chosen {} and the computer has chosen {}. You won!".format(user, computer))
    elif is_loss(user, computer):
        print("You have chosen {} and the computer has chosen {}. You lost".format(user, computer))

def is_loss(user, computer):
    if (user == 'r' and computer == 'p') or (user == 's' and computer == 'r') or (user == 'p' and computer == 's'):
       return True

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False

if __name__ == '__main__':
    instructions()
    while(True):
        print("Choose your option: ")
        print("\t 1. Play with the computer")
        print("\t 2. Exit Game")  
        answer = int(input("Answer: "))
        if answer == 1:
            play()
        elif answer == 2:
          print("Thank you for playing with me! Have a great day")
          sys.exit()   
        while answer not in (1, 2):
          answer = int(input("Answer: "))


# References:
# https://www.askpython.com/python/examples/rock-paper-scissors-in-python-with-ascii-hand
# https://theyuvas.com/rock-paper-scissors-in-python/
# https://www.youtube.com/watch?v=GhPZHvhvlsk&t=24s
# https://maschituts.com/2-ways-to-loop-back-to-the-beginning-of-a-program-in-python/
