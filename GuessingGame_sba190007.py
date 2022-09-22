# CS4395.001 Portfolio Assignment 2: Word guessing game
# Shane Arwood
# September 25, 2022
# Dr. Karen Mazidi
"""
This program analyzes a snippet of anatomy text. It has one function (preprocessing())
that preprocesses the text by tokenizing it and extracting the nouns. The main
function calls the function and uses the returned tokens and nouns to calculate the
50 most common words in the text. The 50 most common words are used in a guessing game
similar to hangman, where the user guesses the word one letter at a time. The user
has points that are adjusted depending on whether the guess was right or not and receives
feedback on teh progress guessing the word.

The program (game) exits when the user has negative points or inputs '!' as a guess
to indicate they want to quit.
"""

import sys
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint


# Function called from main to preprocess the text. It extracts the
# nouns from the text using the WordNetLemmatizer and part of speech
# tagging.
# Parameters: the raw text
# Return: the tokenized text and a list of the nouns in the text.
def preprocessing(text):

    # extract tokens
    lowercase_text = text.lower()
    lower_tokens = word_tokenize(lowercase_text)
    processed_tokens = [t for t in lower_tokens if t.isalpha() and
                        t not in stopwords.words('english') and
                        len(t) > 5]

    # make a list of unique lemmas of the tokens
    token_lemmatizer = WordNetLemmatizer()
    token_lemmas = [token_lemmatizer.lemmatize(t) for t in processed_tokens]
    unique_lemmas = list(set(token_lemmas))

    # pos tagging on the lemmas, adding nouns to a list
    pos_tags = nltk.pos_tag(unique_lemmas)
    print('\nFirst 20 tagged items:', pos_tags[:20])
    pos_nouns = [word for word, pos in pos_tags if pos.startswith('N')]

    # print number of tokens and number of nouns
    print("\nNumber of tokens: ", len(processed_tokens))
    print("\nNumber of nouns: ", len(pos_nouns))

    return processed_tokens, pos_nouns


# Main, which calculates teh lexical diversity of the text then
# preprocesses the text by reading the input file and sending it
# to the preprocessing function. Using the return values from that function,
# it generates a list of the 50 most common words in the text and uses
# those words to implement a guessing game for the user to play.
if __name__ == '__main__':

    # *** PREPROCESSING ***

    # Ensure file name is provided
    if len(sys.argv) < 2:
        print('Please enter the file name as a sys arg.')
        sys.exit()
    else:
        # read input file as raw text and tokenize
        fd = open(sys.argv[1], 'r')
        raw_text = fd.read()
        raw_tokens = word_tokenize(raw_text)

        # calculate lexical diversity
        text_set = set(raw_tokens)
        print("\nLexical diversity: %.2f" % (len(text_set) / len(raw_tokens)))

        # preprocess text, get back tokenized text and nouns
        tokens, nouns = preprocessing(raw_text)

        # construct dict of {noun:count of noun in tokens}
        dict_nouncount = {t: tokens.count(t) for t in nouns}

        # print 50 most common words and their counts and add most common words to list
        sorted_nouncount = sorted(dict_nouncount.items(), key=lambda x: x[1], reverse=True)
        most_common = []
        print('\n50 most common words:')
        for i in range(50):
            print(sorted_nouncount[i])
            most_common.append(sorted_nouncount[i][0])

        # *** GUESSING GAME ***

        # setup
        print('Let\'s play a word guessing game!\n')
        points = 5

        guessed_letters = 0  # count of total guessed letters on each turn, rest to 0 after each guess
        guessed_flag = False  # indicator for when a word has been fully guessed
        list_guesses = []  # list to keep track of letters that have been guessed
        seed(1234)  # to generate random word from teh list of most common words

        # Main loop of game, which generates a new word to guess until the player 'loses'.
        # Each loop resets the game so a new word can be guessed.
        while points >= 0:
            # clear data from previous word
            guessed_flag = False
            list_guesses.clear()

            # generate new word from the most common words in the text
            word = most_common[randint(0, 49)]
            print('_ ' * len(word))

            # Main loop for each round (one round per word). Each loop,
            # the user is prompted to guess a letter. They receive feedback
            # on whether their guess was right of wrong (+ 1 point if right,
            # -1 if wrong). Right guesses display that letter in the word,
            # while the un-guessed words remain underscores. A success message
            # is displayed when the user guesses the whole word and the loop is exited
            # The entire game exits if the player has negative points/enters '!'.
            while points >= 0 and not guessed_flag:
                letter_guess = input('\nGuess a letter:')

                # exit game on indication from player
                if letter_guess == '!':
                    exit()

                # If the player guessed a correct letter, display a message
                # and display the word with that letter in the right positions.
                # Point number is incremented.
                if letter_guess in word:
                    list_guesses.append(letter_guess)
                    points += 1
                    print('Right! Score is', points)

                    # print the updated word with the correct letter guesses
                    for char in word:
                        if char in list_guesses:
                            print(char, end=' ')
                            guessed_letters += 1
                        else:
                            print('_', end=' ')

                    # Case that player has guessed the whole word, will cause exit of this loop
                    if len(word) == guessed_letters:
                        print('\nYou solved it!\nCurrent score: ', points, '\nGuess another word.\n')
                        guessed_flag = True

                    guessed_letters = 0  # reset total guessed letters

                # If the player did not guess a correct letter, decrement the points
                # and display a message. Also check if the player has negative
                # points after this failed guess so the game can be exited.
                else:
                    points -= 1

                    # Player 'lost' the game with negative points
                    if points < 0:
                        print('\nSorry! Negative points, game ending.')

                    # Player has enough points to keep guessing
                    else:
                        print('Sorry, guess again. Score is', points, end=' ')




