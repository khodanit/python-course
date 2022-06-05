"""
18. Write a guessing game that tests the input of a user against any value set to x. 
    - If the guess is correct, print "Correct" to the screen. 
    - If the guess is incorrect print whether the guess was higher or lower than the value to the screen. 
"""

x = 7

y = int(input("Guess any number between 0 and 10: "))

if x == y:
    print("Correct")
elif x > y:
    print("Incorrect. Your guess was lower than the answer")
else:
    print("Incorrect. Your guess was higher than the answer")
