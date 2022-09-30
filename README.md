# CS4395_Portfolio
Portfolio containing class work for CS4395, Human Language Technologies (NLP).

### [Overview of NLP](https://github.com/sba190007/CS4395_Portfolio/blob/33dbf8d2c17d6b8cbd3a62a044ea75d2353614e0/Overview_of_NLP.pdf) 


### Assignment 1: Text Processing With Python
In this assignment, Python was used to reformat an obselete file of employee records. The data file was parsed and converted to a standardized format, pickled, then unpickled to print. It was a good overview of Python's basic text processing capabilities, as well as object oriented programming in Python.

* [Overview](https://github.com/sba190007/CS4395_Portfolio/blob/33a6fcdb4ab6a7bad071452059c618cf556c54c1/Assignment1Overview.pdf)
* [Python Script](https://github.com/sba190007/CS4395_Portfolio/blob/74d995f1f2fa0be7d430b005a9359c9e656a7f17/Homework1_sba190007.py)

### Assignment 2: Exploring NLTK
This assignment served as a helpful introduction to how powerful the Natural Toolkit (NLTK) can be for analyzing documents. In the assignment, text samples are analyzed via NLTK's Text class methods, such as lemmatize, stem, and concordance. It gave me a good idea of why Python is so effective at text processing and how NLTK enhances its capabilities even more. 

* [Colab python notebook](https://github.com/sba190007/CS4395_Portfolio/blob/cc6f7f3119fb8291edfd6f6baf0c7f1024caa25e/CS4395Portfolio2_sba190007ipynb%20-%20Colaboratory.pdf)

### Assignment 3: Guessing Game
This assignment allowed me to practice several different capabilities
of NLTK, including tokening, parts of speech tagging, and lemmatizing.
It was also good practice into writing a user-interactive program. 

A large text is taken in a sysarg, then the text is preprocessed to
extract the most common nouns. Those nouns are used to implement a game similar to hangman, where the user guesses one of the words
one letter at a time and receives feedback. They can keep playing until they get negative points (too many wrong guesses) or input an
exclamation point. 

* [Python script](https://github.com/sba190007/CS4395_Portfolio/blob/a8bde45748fefafef19d0e2a3f4471de8ae7b98a/GuessingGame_sba190007.py)

### Assignment 4: WordNet
This assignment was a great exploration of WordNet for understanding how language is organized. It was intesting to use specific examples to view the noun and verb hierarchies and get to know the different methods available in WordNet. I was particularly impressed with SentiWordNet, since the connotation/emotions behind words are often just as important as their definitions. 

Through this assignment, I was also able to explore different word similarity algorithms, as well as get practice in identifying collocations with the mutual information formlua. 

* [Python notebook](https://github.com/sba190007/CS4395_Portfolio/blob/aa61f164c81372c077823537a2a64fb91a142698/WordNetPortfolioAssignment_sba190007.pdf)

### Assignment 5: N-Grams
This assignment gave me the opportunity to learn about how n-grams are used to form probabilistic language models. Three training corpora in different languages were analysed to create unigram and bigram dictionaries, then those dictionaries were used to predict which language each line in a test file was. The results were compared to the solution containing what language each line was actually written in. 

* [Program 1](https://github.com/sba190007/CS4395_Portfolio/blob/729b4ad508a558a31970f1dfaa330f13414464ed/NGrams_sba190007/Program1_sba190007.py) creates the n-gram dictionaries
* [Program 2](https://github.com/sba190007/CS4395_Portfolio/blob/729b4ad508a558a31970f1dfaa330f13414464ed/NGrams_sba190007/Program2_sba190007.py) uses the dictionaries to build a language model
* The [narrative](https://github.com/sba190007/CS4395_Portfolio/blob/c01a1a8062f6cc0f029546bb0ba79311435a1514/CS4395NGramsNarrative.pdf) is a written reflection on the utility of n-grams and language models.
