import random 

def play_game():
    print_instructions() #this is a function that is passed into play game 
    number_to_guess = random.randint(1,1000) # this could be a way to store the guess based off input on my mystery word 
    number_guessed = False #this is used in the while looop and basically checks to see if gues is true 
    guesses = 0 #we can += to add to to this from an if statement and keep track of guesses 
    while not number_guessed and guesses < 10:
        guess = input_integer("whats your guess? ", min=1, max=1000) # this sets guess to pass INPUT_INTEGER function
        guesses += 1
        count_down = 10 - guesses
        tracking_statement = print(f"You have {count_down} guesses remaining, idiot!")
        if guess == number_to_guess:
            print("Yay your not as dumb as you look! meh fuckoff!")
            number_guessed = True
        elif guess < number_to_guess:
            print("Dude wat, your to low; I don't even stoop to that level. ")
            tracking_statement
            number_guessed = False 
        else:
            print("You must be High!")
            tracking_statement


          
def print_instructions():
    print("guess a number between 1 and 1000.")

def input_integer(prompt, min=None, max=None): # here, als makes sense to have min = none and max = none because that is defined in the guess variable with the Input_Integer fucntion passed to it  
    guess = input(prompt)#takes prompt as argument 
    while not (is_integer(guess) and within_range(int(guess), min, max)): # this while loop takes to functions and passes variable into them 
        print("What the heck I don't understand you!! It says between 1 and 1000 not whaterver the fuck you just put!!")
        guess = input(prompt)
    return int(guess)

def is_integer(string):
    return string.isdigit()

def within_range(number, min=None, max=None):
    """
    Given a possible min and max return true if num in between min and max else return false
    """
    if min is not None and number < min:
        return False 
    if max is not None and number > max:
        return False
    return True

play_game()