"""
19. Improve on the guessing game that tests the input of a user against any value set to x. 
    - If the guess is correct, print "Correct" to the screen. 
    - If the guess is incorrect print whether the guess was higher or lower than the value to the screen. 
    - Incorrect attempts should prompt the user to guess again
    - The game should end on a correct attempt or when the user inputs the string "quit"
"""

x = 7

y = input("Guess any number between 0 and 10 (enter 'quit' to exit): ")

while y != "quit":
    if x == int(y):
        print("Correct")
        y = "quit"
    elif x > int(y):
        print("Incorrect. Your guess was lower than the answer")
        y = input("Guess any number between 0 and 10 (enter 'quit' to exit): ")
    elif x < int(y):
        print("Incorrect. Your guess was higher than the answer")
        y = input("Guess any number between 0 and 10 (enter 'quit' to exit): ")
    else:
        print("Invalid option")
        y = input("Guess any number between 0 and 10 (enter 'quit' to exit): ")

print("Done")
