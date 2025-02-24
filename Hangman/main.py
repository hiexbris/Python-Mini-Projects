import random
from hangman_stages import stages
from hangman_wordlist import word_list
lives = 6
letter = random.choice(word_list)
number = len(letter)
display = ""

for i in range(0, number):
    display += "_"
display = list(display)
for i in range(0, number):
    print(display[i], end='')

while not lives == 0:
    guess = input("\nGuess a letter ").lower()
    t = 0
    for position in range(0, number):
        if guess == letter[position]:
            display[position] = guess
            t += 1
    for i in range(0, number):
        print(display[i], end='')
    if t == 0:
        print("\nNo, you lost a life")
        lives -= 1
    win_checker = display.count("_")
    if win_checker == 0:
        print("\nYou won!")
        break
    print(stages[lives])

if lives == 0:
    print("You lost")
    print(f"The word was {letter}")