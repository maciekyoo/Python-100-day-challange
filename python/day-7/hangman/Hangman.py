# Step 1
from words import word_list
from hangman_art import logo, stages
import random
from tracemalloc import stop
chosen_word = random.choice(word_list)  # choosing random word

print(logo)
lives = 6
display = []
for _ in range(len(chosen_word)):
    display += '_'

end_of_game = False
while not end_of_game:  # loop for checking if every letter is swapped
    guess = input("Guess the letter: ").lower()  # get user input (letter)

    # loop for checking and swaping letters
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(
        # f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(f"{' '.join(display)}")

    print(stages[lives])
