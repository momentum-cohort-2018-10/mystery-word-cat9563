import random
# I ended burning way to much time with tryihg to figure my control flow.
# I didnt complete the other functions I wanted to have for this.


def play_game():
    print_instructions()
    user_input = difficulty_selection_random_word
    word_to_guess = difficulty_selection_random_word(user_input)
    #print_word(word_to_guess, guesses)
    bad_guesses = 0
    #good_guess = []
    prompt = input("enter your guess: ")
    while bad_guesses < 8 and not word_to_guess:
        guess = input_string(prompt)
        print_word(word_to_guess, guess)
        #good_guess.append(guess)
        if guess not in word_to_guess:
            bad_guesses += 1
            count = 8 - bad_guesses
            tracking_statement = print(f"You have {count} guesses remaining.")
            tracking_statement
        else:
            print("nice")

def print_instructions():
    print("Welcome to Mystery Word once you have selected your difficulty level you will have 10 guesses to figure out the word!")
    print("Easy Mode will return a word that is 4 to 6 characters long.")
    print("Normal Mode will return a word that is 5 to 8 characters long.")
    print("Hard Mode will return a word that is 8+ characters")

def input_string(prompt):
    guess = input(prompt)
    #bad_input = False
    while (is_alpha(guess)):  
        print("Invalid input!")
        guess = input(prompt)
    return str(guess)

def is_alpha(string):
    return string.isalpha()
   
def difficulty_selection_random_word(user_input):
    """
    Chooses the random word based of the of the user selection and returns it to the guess fucnctoin
    """
    difficulty = int(input("please type in 1 for easy, 2 for normal or 3 for hard: "))

    user_input = difficulty

    words = []
    with open("words.txt") as words_file:
        for word in words_file.readlines():
            words.append(word.strip())

    # words = []
    easy_words = [e for e in words if len(e) <= 4 and len(e) <= 6]
    med_words = [e for e in words if len(e) >= 5 and len(e) <= 8]
    hard_words = [e for e in words if len(e) >= 8]

    while user_input != range(1,4):
        if user_input == 1:
            return random.choice(easy_words)
        elif user_input == 2:
            return random.choice(med_words)
        elif user_input == 3:
            return random.choice(hard_words)
        else:
            user_input = int(input("Please enter 1, 2, or 3: "))

def display_letter(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"

def print_word(word, guesses):
    letter = guesses
    output_letters = []
    for letter in word:
        output_letters.append(display_letter(letter,guesses))
    print(" ".join(output_letters))



play_game()
