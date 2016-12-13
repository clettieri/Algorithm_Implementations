"""
Various Examples of using Recursion.

Base Case - this is what causes the recursion to stop and actually return a value.
Recursive Case - this is when we call the function on itself.
"""

"""FACTORIAL"""
def factorial(n):
    '''(int) -> int
    
    Will recurisvely computed the factorial of n.
    5! = 5x4x3x2x1
    n! = n * (n-1)!
    '''
    #Base Case
    if n == 1 or n == 0:
        return 1
        
    #Recursive Case
    return n * factorial(n-1)
    
assert factorial(0) == 1
assert factorial(4) == 24
assert factorial(5) == 120
print "Success - Factorial"


"""PALINDROME"""
def is_palindrome(s):
    '''(string) -> bool
    
    Will test if word is a palindrome by recurisvely checking the first and last
    letters to be the same.  Base case is a string of one or zero characters.
    '''
    #Format string
    s = s.upper()    
    
    #Base Case
    if len(s) <= 1:
        return True
    
    #Recursive Case
    if s[0] == s[-1]:
        #First & Last match, test substring
        return is_palindrome(s[1:-1])
    else:
        return False
        
assert is_palindrome("") == True
assert is_palindrome("cat") == False
assert is_palindrome("Rotor") == True
assert is_palindrome("racecar") == True
print "Success - Palindrome"