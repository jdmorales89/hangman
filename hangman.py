import random
import json
import string
from visual_hangman import lives_visual_dict

# random.seed(10) # Use seed if you want to mantain the choiced word

# Opening JSON file
f = open("hangman/words.json")
# Returns JSON object as a list
words = list(json.load(f).values())[0]


def get_valid_word(word_list):
    """Randomly select a word from word_list and check validity (no dashes nor spaces)

    Args:
        word_list (list): List of words to validate

    Returns:
        [str]: Valid word from the word_list
    """
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(word_list)
    return word


def hangman():
    """Play The Hangman game using uppercase letters"""
    word = get_valid_word(words).upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # alphabet
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        if len(used_letters) != 0:
            print(
                "\nYou have",
                lives,
                "attempts left and you have used these letters: ",
                " ".join(used_letters),
            )
        else:
            print("\nYou have", lives, "attempts left")

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("\nCurrent word: ", " ".join(word_list))
        print(lives_visual_dict[lives])

        input_letter = input("Guess a letter: ").upper()
        if input_letter in alphabet - used_letters:
            used_letters.add(input_letter)
            if input_letter in word_letters:
                word_letters.remove(input_letter)
                print("Correct! letter is in word!")
            else:
                lives -= 1  # take away a life if wrong
                print("Letter is not in word!")
        elif input_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")

    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print("\nYou died, sorry. The word was:", word)
    else:
        print(f"\nYou guessed the word {word}!")


hangman()
