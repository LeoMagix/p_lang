"""The programs ask user to guess a number randomly selected by the program and 
    provides certain clues to help our user guess number."""

#Call the random moduke to help with supplying arbitrarily chosen numbers
from random import randint

#Variable to store our arbitrary values
arbiter = randint(1, 20)

#moved the bulk of our code to the function guess_num
def guess_num(random_num):
    """
    Call the user to enter a number till its correct.
    And give the player some clues to get it right.
    """
    flag = True             #Create a Flag for the while loop

    #Variable for computing number of guesses it took
    guessometer = 0

    while flag:
        guess = int(input("Pick a Number from 1 to 20:\n"))
        print()         #Just for readability purposes

        if guess == random_num:
            guessometer += 1
            if guessometer == 1:
                print(f"Wow! You guessed my number in {guessometer} guess!")
        
            else:
                print(f"Good job! You guessed my number in {guessometer} guesses!")

            flag = False        #Prevent an infinite while loop

        elif guess != random_num:
            if guess < random_num:     #Gives user a clue
                print("Your guess is too low.")
                print()
                guessometer += 1

            elif guess > random_num:   #Gives user a clue-that is guess lower
                print("Your guess is too high.")
                print()
                guessometer += 1    

guess_num(arbiter)
