from ast import ClassDef, If
from operator import index, truediv
import os
from sre_constants import JUMP
from time import sleep
def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    
def split(secret_word):
    return list(secret_word)



    
                                           # HangMan Project
def welcome_msg():                                    
    cls()
    print("\t\t\t\t\t\t\t\t------------------------------------\n")
    print("\t\t\t\t\t\t\t\t\tWELCOME TO HANGMAN\n")
    print("\t\t\t\t\t\t\t\t------------------------------------\n")



welcome_msg()

sleep(2)

# To GET PLAYERS 
print("\n")
print("\tEnter Name Of Player")
player_1 = input("\tName of Puzzle Giver: ")

sleep(1)

print("\n")
print("\tEnter Name Of Player")
player_2 = input("\tName of Puzzle Guesser: ")
#---------------------------------------------




sleep(0)
cls()


print("Welcome: " + player_1 +" and " + player_2 + "!\n")

secret_word = input( player_1 + " Type in a Secret Word to be guessed: ")


if len(secret_word) == 0 or secret_word.__contains__ (int):
        print("Invalid Input, Try a letter\n")
else:
    display_dash = "_" * len(secret_word[1:-1]) 
    cls()

print(player_2 + " Time to Guess\nYou have 6 tries to guess correct letters untill the man is hanged")
cls()

print("This is a " + str(len(secret_word)) + " letter word")
print( secret_word[0] + display_dash + secret_word[-1])


limit = 6
guessed_ltr =""

while limit > 0 :
    print("")
    guess = input(" Guess a letter in the word: ")
    
    if guess in secret_word :
       sleep(1)
       cls()
       print("Correct! There is a " + guess + " in the secret word")
       print(f"You have {limit} lives left")
       
       
     
            
    else:
        limit -=1
        print("")
        cls()
        print(guess + " is not in secret word")
        
        
        print("")
        print("You have " + str(limit)+ " lives left")
        if limit == 5:
           print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        
        elif limit== 4:
            
            print
            
            sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif limit == 3:
            print
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")

        elif limit == 2:
            print
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif limit == 1:
            print
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |        \n"
                  "__|__\n")
        elif limit == 0:
            print
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")                
    
    
    
    guessed_ltr = guessed_ltr + guess
    wrong_ltr_cont = 0
    
    

    for letter in secret_word:
        if letter in guessed_ltr:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrong_ltr_cont +=1
    if wrong_ltr_cont == 0:
        cls()
        print(f" Congratulation YOU WON! the word was: {secret_word}")
        break
            
            
    
            

    
    


wait = input()

