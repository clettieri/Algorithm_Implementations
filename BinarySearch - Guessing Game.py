"""
Binary Search - Pick a Number Guessing Game!

In this game you will define a range from 1 to n.
Then you must pick a number in that range.
The computer will tell you how many guess at most it will
need to guess your number.

Each guess the computer makes the user will say if their number
is higher, lower, or exactly right.

This game is a demonstration of binary search.
Binary search find's an element in a sorted list by continually halving
the search space until the element is found.
"""
import math

#Global Variables
MAX_RANGE = None
GUESSES_NEEDED = None

def start_game():
    '''(None) -> None
    
    This function will print the instructions to the screen, and get the
    range high from the user.  It will then state how many guesses
    the computer will need and the game will begin.  This will
    set our global variable MAX_RANGE given the user's input.
    '''
    global MAX_RANGE
    print "Welcome to the Binary Search - Pick a Number Guessing Game!"
    print "All you have to do is pick a range from 1 to Any Positive Number"
    print "And then pick a number in the range.  After each guess I make, "
    print "please tell me if your guess is higher, lower, or if I guessed right!"
    print ""
    
    #Get upper range from User
    while True:
        try:
            print "What is the maximum range you want to play in, from 1 to ?"
            MAX_RANGE = int(raw_input(">"))
        except ValueError:
            print "That was not a valid number, please try again."
            continue
        else:
            GUESSES_NEEDED = compute_total_guesses(MAX_RANGE)
            print "Very well, I will need " + str(GUESSES_NEEDED) + " guesses."
            break
    print ""
    print "Now pick a number between 1 and " + str(MAX_RANGE) +  ", write it down!"
    print "Press Enter when you have decided upon a number"
    print ""
    print raw_input()
    guess()
    
def compute_total_guesses(n):
    '''(integer) -> integer
    
    Given a maximum value for the range starting from 1, this will
    return the maximum number of guesses the computer needs.  The
    formula is max_guesses = log base 2 of n.
    '''
    guesses = math.log(n, 2)
    return int(math.ceil(guesses))
    
def guess():
    '''(None) -> None
    
    Now the game has begun and the computer will continue to guess until
    the number is found or the entire space has been searched in our number
    of guesses we promised.
    
    This function will utlize binary search to continually halve the search space
    from 1 to MAX_RANGE until the user's number is found.
    '''
    current_max = MAX_RANGE
    current_min = 1
    guess_count = 1
    while True:
        #Make guess
    
        # **** BINARY SEARCH **** 
        current_range_difference = current_max - current_min
        current_guess = (current_range_difference / 2) + current_min 
        # ***********************
        
        #Get Input
        print ""
        print "My guess #"+str(guess_count)+" is: " + str(current_guess)
        print "Is your number higher(H), lower(L), or was I correct(C)?"
        print ""
        #Input Loop
        while True:
            user_input = raw_input(">")
            if user_input[0].upper() not in ["H", "L", "C"]:
                print "Invalid input, please type H, L, or C."
            else:
                #Have valid response
                guess_count += 1
                break
        #Analyze guess
        user_choice = user_input[0].upper()
        if user_choice == "H":
            #User number is higher
            current_min = current_guess
        elif user_choice == "L":
            #User number is lower
            current_max = current_guess
        elif user_choice == "C":
            print "I told you I could do it!"
            print "Exiting.."
            break
        elif guess_count > GUESSES_NEEDED:
            print "You must be cheating, or did you forget your number?"
            print "Exiting.."
            break
    
start_game()