import os
import re
from time import sleep
def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    

def welcome_msg(): 

    # THIS FUNCTION DISPLAYS A SIMPLR GUI WELCOME MESSAGE                                   
    cls()
    print("\t\t\t\t\t\t\t\t------------------------------------\n")
    print("\t\t\t\t\t\t\t\t\tWELCOME TO HANGMAN\n")
    print("\t\t\t\t\t\t\t\t------------------------------------\n")
    #-----------------------------------------------------------


def main_vars_get_plys ():
    
    #THIS FUNCTION GETS PLAYER NAMES
    
    global player_1
    global player_2
    
    
    


    # To GET PLAYERS 
    print("\n")
    print("\tEnter Name Of Player")
    player_1 = input("\tName of Puzzle Giver: ")

    sleep(1)

    print("\n")
    print("\tEnter Name Of Player")
    player_2 = input("\tName of Puzzle Guesser: ")

    cls()

    print("Welcome: " + player_1 +" and " + player_2 + "!\n")

    

    cls()

    
def get_guess():
    # THIS FUCTION GETS A SECRET WORD AND CHECKS IF IT CONTAINS DIGITS FROM PLAYER 1 TO BE GUESSED BY PLAYER 2
    global secret_word
    
    secret_word = (input( player_1 + " Type in a Secret Word to be guessed: "))
    
    if not secret_word.isalpha():
        cls()
        print( player_1 + " The word should not contain numbers ")
        sleep(1)
        cls()
        get_guess()
    
    if secret_word =="" :
        cls()
        print("Invalid input. Secret word cannot be blank. ")
        sleep(1)
        cls()
        get_guess

    



def pre_game_msg ():

    

    display_dash = "_" * len(secret_word[1:-1]) 
    cls()

    print(player_2 + " Time to Guess\nYou have 6 tries to guess correct letters untill the man is hanged")
    sleep(2)
    cls()

    print("This is a " + str(len(secret_word)) + " letter word")
    print( secret_word[0] + display_dash + secret_word[-1]) 


def main_loop():

    # THIS IS THE MAIN BLOCK OF CODE FOR THE LOGIC OF THE GAME
    limit = 6
    guessed_ltr =""
    
    

    while limit > 0 :
        print("")
        guess = input(" Guess a letter in the word: ")
        
    
        if guess  in  secret_word :
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
    
    

        for letter in  secret_word:
            if letter in guessed_ltr:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                wrong_ltr_cont +=1
        if wrong_ltr_cont == 0:
            cls()
            print(f" Congratulation YOU WON! the word was: {secret_word}")
            break
    
    

    
def play_loop():

    #THIS FUNCTION IS TO PLAY THE GAME AGAIN OR EXIT
    
    cls()
    
    play_game = input("Do You want to play again? y = yes, n = no \n" ":")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n"  ":")
    if play_game == "y" :
        
        cls()
        sleep(1)
        
        main_vars_get_plys()

        sleep(2)
        cls()


        get_guess()
        pre_game_msg()
        main_loop()

        play_loop()
    elif play_game == "n" :

        cls()
        sleep(1)
        
        print("Thanks For Playing! We expect you back again!")
        



# ALL FUNCTIONS WHERE CALLED HERE
welcome_msg()

sleep(2)

main_vars_get_plys()

sleep(2)
cls()


get_guess()
pre_game_msg()
main_loop()

sleep(2)

play_loop()

    
wait = input()

