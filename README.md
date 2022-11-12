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

### Assignment 6: Web Crawler
This assignment resulted in a knowledge base about cakes/baking from the Preppy Kitchen's blog and associated webpages. Web crawling and web scraping functions were used to crawl the blog and extract key terms, then use those terms to create a dictionary of sentences containing those terms. Beautiful Soup and NLTK were used to extract the text from the pages and process them. 

* [Python script](https://github.com/sba190007/CS4395_Portfolio/blob/ebb59a2f3456bf9f678f06c10cadbd3be794c86a/WebCrawler_sba190007/WebCrawler_sba190007.py) crawls from a starting link and creates a knowledge base by scraping relevant links.
* The [report](https://github.com/sba190007/CS4395_Portfolio/blob/ebb59a2f3456bf9f678f06c10cadbd3be794c86a/WebCrawler_sba190007/CS4395WebCrawlerReport_sba190007.pdf) displays the knowledge base, discusses how the knowledge base was created, and provides a sample dialog that could be created with a chatbox and the knowledge base. 

### Assignment 7: Syntax Parsing
Rather than a program, this assignment was more an exploration into various types of syntax parsing for sentences. The example sentence:

"The mouse baked a small cookie by mixing flour and sugar in a yellow bowl"

is used to demonstrate a PSG tree, dependency parse, and SRL parse. The various relations, modifiers, and other terms that relate the parts of the sentence for each parse are defined as well. 

* The [document](https://github.com/sba190007/CS4395_Portfolio/blob/d6216457bc0298eff090d3b0faed39bae3744859/CS4395Portfolio_SyntaxParsing_sba190007.pdf) uses the example sentence to conceptually understand the various parses and includes a reflection on the pros and cons of each parse. 

### Assignment 8: Author Attribution
This assignment was my first experience using machine learning tools. A csv file containing a collection of the Federalist Papers along with their authors is given to the program, which converts the author column into categorical data. Train and test are divided, with 80% in train, then are input into the Naive Bernoulli Bayes model, logistic regression, and a neural network. The accuracies of the predictions are compared.

* The [Python notebook](https://github.com/sba190007/CS4395_Portfolio/blob/9f8ceb7711783bf0679fca69554154b53406c7e9/CS4395AuthorAttribution_sba190007.ipynb%20-%20Colaboratory.pdf) was written in Google Colab and demonstrates various methods of going about author attribution using tools from sklearn.

https://github.com/sba190007/CS4395_Portfolio/blob/b58b155f51f8d67061b447c473dd9f9e4630ab13/CS4395_ACLPaperSummary_sba190007.pdf

### Assignment 9: Chatbot
This assignment was to create a chatbot. My project is called BakeBot, a chatbot that converses with the user about baking. BakeBot can tell the user what recipes it knows as well as the tools needed to bake, specific ingredients like flour and sugar, how they are combined to make batter, and how long the batter should bake for. Its knowledge base was derived from a previous portfolio assignment where the blog of baker John Kanell of Preppy Kitchen (https://preppykitchen.com/) was crawled to find the most commonly used terms in baking recipes and examples of sentences associated with them. BakeBot is also trained with user inputs when the user expresses something that can be used for a personalized response (such as a like or dislike).

BakeBot was created using ChatterBot (https://chatterbot.readthedocs.io/en/stable/#), a Python library that implements machine learning algorithms to select the best response to a user input based on training lists of example conversations. ChatterBot is not currently being maintained which resulted in many dependency issues, so I used a previous version of ChatterBot that is compatible with spaCy. NLTK was used as well.

* [Report] (https://github.com/sba190007/CS4395_Portfolio/blob/9ce5d8b7307ef0fd14dc71191eb9ef28aee94f77/CS4395_Chatbot_sba190007/CS4395_ChatBotReport_sba190007.pdf)
* [Code] (https://github.com/sba190007/CS4395_Portfolio/blob/9ce5d8b7307ef0fd14dc71191eb9ef28aee94f77/CS4395_Chatbot_sba190007/cs4395_chatbot_sba190007.py) (Python, written in Google Colab)

### Assignment 10: ACL Paper Summary
This [ACL paper summary] (https://github.com/sba190007/CS4395_Portfolio/blob/b58b155f51f8d67061b447c473dd9f9e4630ab13/CS4395_ACLPaperSummary_sba190007.pdf) was an extremely interesting look into NLP outside of this class, specifially ACL conferences where so much learning and sharing of work is being done to contribute to NLP. I chose this paper about the TellMeWhy dataset that aims to address why-questions in narratives because it described a section of NLP where there is an integration of common knowledge, fiction, and understanding of character motive in texts. I love reading and was very excited to see the work being done for reasoning in stories. Reasoning is such a human skill and this paper seems like a great leap forward in applying this to technology. 