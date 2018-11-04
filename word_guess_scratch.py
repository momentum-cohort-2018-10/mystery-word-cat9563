import random


def input_string(prompt): # here, als makes sense to have min = none and max = none because that is defined in the guess variable with the Input_Integer fucntion passed to it  
    guess = input(prompt)#takes prompt as argument 
    #bad_input = False
    while (is_alpha(guess)):  # this while loop takes to functions and passes variable into them 
        print("Invalid input!")
        guess = input(prompt)
    return str(guess)

def is_alpha(string):
    return string.isalpha()

print(input_string("h"))





# def play():
#     word = "Grandma"
#     guesses = str(input("whats your guess: "))
#     bad_guess = False

# def display_letter(letter, guesses):
#     if letter in guesses:
#         return letter
#     else:
#         return "_"


# def print_word(word, guesses):
#     letter = guesses
#     output_letters = []
#     for letter in word:
#         output_letters.append(display_letter(letter,guesses))
#     print(" ".join(output_letters))

# print_word(word, guesses)
# #side notes 
# # easy_words = []
#     # for e in words: 
#     #     if e <= 4:
#     #         easy_words.append(e)