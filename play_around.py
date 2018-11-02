import random

words = []


with open("words.txt") as words_file:
    for word in words_file.readlines():
        words.append(word.strip())
    # easy_words = []
    # for e in words: 
    #     if e <= 4:
    #         easy_words.append(e)
    easy_words = [e for e in words if len(e) <= 4 and len(e) <= 6]
    med_words = [e for e in words if len(e) >= 5 and len(e) <= 8]
    hard_words = [e for e in words if len(e) >= 8]

print(random.choice(easy_words))
print(random.choice(med_words))
print(random.choice(hard_words))


