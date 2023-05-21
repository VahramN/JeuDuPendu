# This is the game Hangman.
# The player must guess the word with maximum 6 chances, otherwise the game is lost.
import random
# word list file. each line is 1 word
WORD_FILE = "mots_pendu.txt"
# Player failure chances before the lost
CHANCES = 6


# Choose from the given list words one random word and return it.
def choose_word(words):
    return random.choice(words)


# Open the file, randomly choose a line, return the content and close the file
def read_random_line_in_file():
    # read the content of the file in the list
    with open(WORD_FILE, "r") as word_file:
        lines = word_file.readlines()
    # select randomly a word
    selected_word = choose_word(lines)
    # close a file
    word_file.close()
    # return the word, cleaned from new line
    return selected_word.strip()


# Find all the occurrences' indexes of the subtext in the given text
def find_all_occurrences(main_text, sub_text):
    # make both words in lower case to be able to compare correctly
    main_text = main_text.lower()
    sub_text = sub_text.lower()
    # final result list
    result = []
    # starting position
    position = 0

    # loop until the returned position is -1
    while True:
        position = main_text.find(sub_text, position)
        if position >= 0:
            result.append(position)
            position += len(sub_text)
        else:
            break

    return result


# the main function of playing the game
def play_game():
    # start with random word from the file
    word = read_random_line_in_file()
    # keep the length
    word_length = len(word)
    print(f"Playing 'Jeu du pendu'. You have {CHANCES} possibilities to find the word.")
    # print(word)  # For debugging purpose uncomment the line

    # construct a word with the same length and the characters '_'
    underscore_word = "_" * word_length
    # keep in the character list
    word_char_list = [*underscore_word]

    # failure counter
    fail_quantity = 0
    print(f"{''.join(word_char_list)}   (chances {CHANCES - fail_quantity})")
    # if failure limit is not riched and the player did not guess all characters, need to loop
    while (fail_quantity < CHANCES) and ('_' in word_char_list):
        # read the character
        character = input("Please enter the character: ")

        # character validation. If not repeat.
        if not(character.isalpha() and len(character) == 1):
            print("Please enter ONE ALPHABETIC character: ")
            continue

        # Find all occurrences
        found_char_indexes_list = find_all_occurrences(word, character)
        # if the letter is found
        if len(found_char_indexes_list) > 0:
            for i in found_char_indexes_list:
                # replace '_' in word_char_list in index i with the real character
                word_char_list[i] = word[i]
            print(f"Letter {character} is found.")
        # if the letter is not found
        else:
            # increment the failure quantity
            fail_quantity += 1
            print(f"Letter {character} is NOT found.")

        print(f"{''.join(word_char_list)}   (chances {CHANCES - fail_quantity})")

    if fail_quantity < CHANCES:
        print(f"You WIN the game.")
    else:
        print(f"You LOST the game. The word is {word}.")


# Call and start the game
play_game()
