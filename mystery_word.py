import random


def start_mystery_word():
    """
    Starts game
    """
    difficulty_selection_random_word
    store_random_word
    greet = int(input(""" Welcome to Mystery Word please select a difficulty level between 1 and 3: """))
    return difficulty_selection_random_word(greet)
    return store_random_word

def difficulty_selection_random_word(user_input):
    """
    Chooses the random word based of the of the user selection and returns it to the guess fucnctoin
    """
    user_input = start_mystery_word
    words = []
    with open("words.txt") as words_file:
        for word in words_file.readlines():
            words.append(word.strip())

    
def store_random_word(user_input):
    user_input = difficulty_selection_random_word
    words = []
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


start_mystery_word()

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print('Too small')
#         continue
#     print('Input is of sufficient length')
#     # Do other kinds of processing here...



# number = 23
# running = True

# while running:
#     guess = int(input('Enter an integer : '))

#     if guess == number:
#         print('Congratulations, you guessed it.')
#         # this causes the while loop to stop
#         running = False
#     elif guess < number:
#         print('No, it is a little higher than that.')
#     else:
#         print('No, it is a little lower than that.')
# else:
#     print('The while loop is over.')
#     # Do anything else you want to do here

# print('Done')
