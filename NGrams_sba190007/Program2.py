import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import pickle


# Function to calculate the probability of a line being in a certain language.
# It takes the bigrams of the test document, the nigram and bigrams dictionaries for
# the given language, and the vocab size, then calculates and returns the probability
# using laplace smoothing.
def probability(bigrams_test, unigram_dict, bigram_dict, vocab_size):
    laplace_prob = 1

    # calculate probability with Laplace smoothing: (b + 1) / (u + v) where b is
    # the bigram count, u is the unigram count of the first word in the bigram, and v
    # is the total vocabulary size
    for bigram in bigrams_test:
        if bigram in bigram_dict:
            b = bigram_dict[bigram]
        else:
            b = 0
        if bigram[0] in unigram_dict:
            u = unigram_dict[bigram[0]]
        else:
            u = 0

        laplace_prob = laplace_prob * ((b + 1) / (u + vocab_size))

    return laplace_prob


# Main, which opens the test, solution, and result files. The unigram and bigram dictionaries
# are unpickled then used to calculate the laplace probabilities for each language for each
# line in the test file. The result file containing the predictions is compared to the result
# files, and the accuracy and number of incorrect predictions is output.
if __name__ == '__main__':
    # Open test file and remove newlines
    test_fd = open("LangId.test", 'r')
    test_file = test_fd.readlines()
    paragraph_text = []
    for line in test_file:
        paragraph_text.append(line.replace("\n", " "))

    # Open solution file and declare counter for incorrect guesses
    solution_fd = open("LangId.sol", 'r')
    solution_file = solution_fd.readlines()
    incorrect_num = 0

    # Create file to write probability of each language for each line in test file
    results_fd = open("lang_probabilities.txt", "w")

    # Declare counter to keep track of lines in the test file
    line_count = 1

    # Unpickle the 6 dictionaries
    eng_uni_dictionary = pickle.load(open('eng_uni_dictionary.p', 'rb'))
    eng_bi_dictionary = pickle.load(open('eng_bi_dictionary.p', 'rb'))
    ital_uni_dictionary = pickle.load(open('ital_uni_dictionary.p', 'rb'))
    ital_bi_dictionary = pickle.load(open('ital_bi_dictionary.p', 'rb'))
    fr_uni_dictionary = pickle.load(open('fr_uni_dictionary.p', 'rb'))
    fr_bi_dictionary = pickle.load(open('fr_bi_dictionary.p', 'rb'))

    # Calculate total vocabulary size
    total_vocab_size = len(eng_uni_dictionary) + len(ital_uni_dictionary) + len(fr_uni_dictionary)

    # Main loop for calculating probabilities: for each line in the text file, the unigrams and
    # bigrams are found and sent to the probability() function which returns the probability of
    # the line being in a certain language. For each line, the language with the highest probability
    # is written to the result file and the incorrect_num counter is incremented if it doesn't
    # match the solution file.
    for line in test_file:
        # Get unigrams and bigrams
        test_unigrams = word_tokenize(line)
        test_bigrams = list(ngrams(test_unigrams, 2))

        # Calculate the probability of the line being in each of the three languages
        eng_prob = probability(test_bigrams, eng_uni_dictionary, eng_bi_dictionary, total_vocab_size)
        ital_prob = probability(test_bigrams, ital_uni_dictionary, ital_bi_dictionary, total_vocab_size)
        fr_prob = probability(test_bigrams, fr_uni_dictionary, fr_bi_dictionary, total_vocab_size)

        # Find language with the highest probability
        if eng_prob > ital_prob and eng_prob > fr_prob:
            max_lang = "English"
        elif ital_prob > eng_prob and ital_prob > fr_prob:
            max_lang = "Italian"
        elif fr_prob > eng_prob and fr_prob > ital_prob:
            max_lang = "French"
        else:
            max_lang = "Not calculated"

        # Write language with highest probability to the result file
        results_fd.write(str(line_count) + " " + str(max_lang) + "\n")

        # Check if prediction was wrong, then increment incorrect_num (or not)
        if solution_file[line_count - 1] != str(str(line_count) + " " + str(max_lang) + "\n"):
            incorrect_num += 1

        line_count += 1

    # Output accuracy of the predictions and the number of lines incorrectly predicted
    correct = 300 - incorrect_num
    accuracy = correct / 300
    print("Accuracy: " + "{0:.2}".format(accuracy))
    print("Incorrect: " + str(incorrect_num))
