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

def start_game():
    '''(None) -> integer
    
    This function will print the instructions to the screen, and get the
    range high from the user.  It will then state how many guesses
    the computer will need and the game will begin.
    '''
    print "Welcome to the Binary Search - Pick a Number Guessing Game!"
    print "All you have to do is pick a range from 1 to Any Positive Number"
    print "And then pick a number in the range.  After each guess I make, "
    print "please tell me if your guess is higher, lower, or if I guessed right!"
    print ""
    while True:
        try:
            print "What is the maximum range you want to play in, from 1 to ?"
            max_range = int(raw_input(">"))
        except ValueError:
            print "That was not a valid number, please try again."
            continue
        else:
            guesses_needed = compute_guesses(max_range)
            print "Very well, I will need " + str(guesses_needed) + " guesses."
            break
    
        
    

def compute_guesses(n):
    '''(integer) -> integer
    
    Given a maximum value for the range starting from 1, this will
    return the maximum number of guesses the computer needs.  The
    formula is max_guesses = log base 2 of n.
    '''
    guesses = math.log(n, 2)
    return int(math.ceil(guesses))
    
start_game()