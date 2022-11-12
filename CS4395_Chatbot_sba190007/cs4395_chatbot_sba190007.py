"""
The chatbot was written in Google Colab with the ChatterBot Python Library,
NLTK, and spaCy. The program requires the attached knowledge_base_dict.p to
be in the same directory to be run. 
"""

pip install chatterbot2

pip install -U spacy

import os 
import nltk
import pickle
import spacy
ner = spacy.load('en_core_web_sm')
from nltk.corpus.reader.tagged import word_tokenize
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# user object to personalize chatbot
class user_model:
  name = ""
  likes = []
  dislikes = []

# create lists of synonyms to detect user likes and dislikes
like_syns = []
for syn in wordnet.synsets("like"):
    for word in syn.lemmas():
        like_syns.append(word.name())
like_syns = set(like_syns)
      
dislike_syns = []
for syn in wordnet.synsets("dislike"):
    for word in syn.lemmas():
        dislike_syns.append(word.name())
dislike_syns = set(dislike_syns)

# to parse the noun/verb that is liked or disliked
nouns_verbs = ["NN", "NNS", "VB", "VBG"]

# default response until bakebot earns more about the user to
# carry the convetsation when it gets stuck
default_res = "i only know about baking!"

# create bakebot and user
BakeBot = ChatBot('BakeBot',    
                  logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': default_res,
            'maximum_similarity_threshold': 0.4
        }])
User = user_model()

# Train BakeBot in recipes terms
trainer = ListTrainer(BakeBot)

with open('knowledge_base_dict.p', 'rb') as handle:
    knowledge = pickle.load(handle)

for key in knowledge:
    trainer.train(knowledge[key])

# Train BakeBot in formalities
knowledge["formalities"] = [
    "hello",
    "howdy",
    "nice to meet you",
    "i like to bake.",
    "i like baking too.",
    "i want to bake.",
    "thank you.",
    "happing baking!"
]
trainer.train(knowledge["formalities"])

# get user name and start conversation
user_chat = input("you: ")
print("bakebot: i am bakebot. what's your name?")
user_chat = input("you: ")

# detect name, full name must be given
spacy_obj = ner(user_chat)
for entity in spacy_obj.ents:
    if entity.label_ == "PERSON":
        User.name = entity.text
# if full name not given, just use what was input
if User.name == "":
    User.name = user_chat

print("bakebot: hello", User.name, ", let's talk about baking! i can tell you " 
      + "about recipes, ingredients, and the process. say 'bye' to end the chat.")

# main loop for reading user input and responding
while (True):
    user_chat = input("you: ")

    # user input to lower 
    user_chat = user_chat.lower()

    # add details to user model by parsing input
    input_tokens = word_tokenize(user_chat)
    user_chat_pos = nltk.pos_tag(input_tokens)

    # user expressed a like
    for like_syn in like_syns:
        if like_syn in input_tokens:
          for word in user_chat_pos:
              # add the like to the model and train bakebot
              if word[1] in nouns_verbs and word[0] != "i" and word[0] not in like_syns:
                  User.likes.append(word[0])
                  like_response = "wait, you like "+ word[0] + "?"
                  trainer.train([user_chat, like_response])
                  default_res = like_response # come back to personalized response when bakebot is stuck
    # user expressed a dislike
    for dislike_syn in dislike_syns:
        if dislike_syn in input_tokens:
          for word in user_chat_pos:
              # add the dislike to the model and train bakebot
              if word[1] in nouns_verbs and word[0] != "i" and word[0] not in dislike_syns:
                  User.dislikes.append(word[0])
                  dislike_response = "wait, you don't like "+ word[0] + "?"
                  trainer.train([user_chat, dislike_response])
                  default_res = dislike_response # come back to personalized response when bakebot is stuck

    # exit if user wants to stop conversation
    if (user_chat == 'bye'):
        print ("bakebot: bye", User.name, "!")
        break

    # print bakebot's response
    response = BakeBot.get_response(user_chat)
    print ("bakebot: ", response)

# write user model to a text file
fd_write = open("user_model.txt", 'w+')
to_write = "Name: " + str(User.name) + "\n"
fd_write.write(to_write)
to_write = "Likes" + str(User.likes) + "\n"
fd_write.write(to_write)
to_write = "Dislikes" + str(User.dislikes) + "\n"
fd_write.write(to_write)

# print info collected from user
print("Name: ", User.name)
print("Likes", set(User.likes))
print("Dislikes", set(User.dislikes))