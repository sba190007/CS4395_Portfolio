import nltk
from nltk import word_tokenize
from nltk.util import ngrams
import pickle


# Function to create a dictionary of unigrams and one of bigrams
# from a training document in a given language which is passed as an argument.
# The file is opened, the newlines ar eremoved, and the dictionaries are created
# and returned.
def create_dictionaries(filename):
    # Open file and remove new lines
    fd = open(filename, 'r')
    raw_text = fd.readlines()
    paragraph_text = []
    for line in raw_text:
        paragraph_text.append(line.replace("\n", " "))

    # Create dict of unigrams
    unigrams = word_tokenize(str(paragraph_text))
    unigrams_dict = {t: unigrams.count(t) for t in set(unigrams)}

    # Create dict of bigrams
    bigrams = list(ngrams(unigrams, 2))
    bigrams_dict = {t: bigrams.count(t) for t in set(bigrams)}

    return unigrams_dict, bigrams_dict


# Main, which calls create_dictionaries for each of the language training documents,
# then pickles the 6 dictionaries.
if __name__ == '__main__':
    # Create dictionaries of bigrams/unigrams for each language
    eng_unigrams, eng_bigrams = create_dictionaries("LangId.train.English")
    ital_unigrams, ital_bigrams = create_dictionaries("LangId.train.Italian")
    fr_unigrams, fr_bigrams = create_dictionaries("LangId.train.French")

    # Pickle the 6 dictionaries
    pickle.dump(eng_unigrams, open('eng_uni_dictionary.p', 'wb'))
    pickle.dump(eng_bigrams, open('eng_bi_dictionary.p', 'wb'))
    pickle.dump(ital_unigrams, open('ital_uni_dictionary.p', 'wb'))
    pickle.dump(ital_bigrams, open('ital_bi_dictionary.p', 'wb'))
    pickle.dump(fr_unigrams, open('fr_uni_dictionary.p', 'wb'))
    pickle.dump(fr_bigrams, open('fr_bi_dictionary.p', 'wb'))
