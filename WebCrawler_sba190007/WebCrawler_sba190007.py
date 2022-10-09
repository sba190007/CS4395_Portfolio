import requests
from bs4 import BeautifulSoup
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
import pickle

# sets of links used to crawl the webpages and keep
# track of what has been crawled already and what is
# available
links = set()
crawled_links = set()


# Function to recursively crawl a webpage.
# Takes as arguments a starting url from which to crawl
# and a count, which is used as a base case for the
# recursion as a limited number of links are required
# and crawling the whole site results in very slow runtime.
def web_crawler(url_, count_):
    # create soup object
    page = requests.get(url_)
    soup = BeautifulSoup(page.content, 'html.parser')

    # crawl the first link and use recursion to crawl
    # the first link found
    for link in soup.find_all('a'):
        # Add each link found to a list
        if link.get('href').startswith('https'):
            links.add(link.get('href'))

            # Crawl the first link found on the starting page
            if link.get('href') not in crawled_links and count_ < 2:
                count_ += 1
                crawled_links.add(link.get('href'))
                web_crawler(link.get('href'), count_)


# Function to scrape the text off a webpage and
# write the raw text to a file, takes the url and
# filename to write to as arguments.
def web_scraper(url_, filename_):
    # create soup object
    page = requests.get(url_)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_text = ''

    # find the main text in the page and add it to a string
    for paragraph in soup.find_all('p'):
        main_text += paragraph.get_text()

    # write the text to a file
    fd = open(filename_, 'w+')
    fd.write(main_text)
    fd.close()


# Function to read text from a file and return
# the sentence tokens from the file. Takes the
# filename as a argument.
def cleanup_text(filename_):
    # process text by removing tabs and newlines and lowercasing
    fd = open(filename_, 'r')
    raw_text = fd.read()
    raw_text = raw_text.replace('\n', ' ')
    raw_text = raw_text.replace('\t', ' ')
    raw_text = raw_text.lower()

    fd.close()

    sentences_ = sent_tokenize(raw_text)
    return sentences_


if __name__ == "__main__":
    term_frequency_dict = {}
    knowledge_dict = {}
    URL = "https://preppykitchen.com/category/recipes/desserts/cakes/"
    web_crawler(URL, 0)

    # add the first 20 crawled links
    # to a list of urls
    urls = list(links)[:15]
    print(urls)

    # write raw contents of the crawled webpages to files
    file_no = 0
    for url in urls:
        file_no += 1
        filename = "url" + str(file_no) + "raw.txt"
        web_scraper(url, filename)

    # read content from raw text files, cleanup and write to new
    # files
    file_no = 0
    while file_no < 15:
        file_no += 1
        file_to_read = "url" + str(file_no) + "raw.txt"
        sentences = cleanup_text(file_to_read)

        file_to_write = "url" + str(file_no) + "sentences.txt"
        fd_write = open(file_to_write, 'w+')
        fd_write.write(str(sentences))

     # Create the term frequency dictionary by reading the file,
    # processing the text and word tokenizing it, then counting the counts
    # if words found in the files.
    file_no = 0
    while file_no < 15:
        # open file
        file_no += 1
        file_to_read = "url" + str(file_no) + "sentences.txt"
        fd_read = open(file_to_read, 'r')

        # process text and word tokenize
        text = fd_read.read()
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]
        tokens = [t.replace('\n', '') for t in tokens]
        tokens = [t.replace('\t', '') for t in tokens]
        tokens = [t.lower() for t in tokens]

        # count the tokens and put results into the term
        # frequency dict
        for term in tokens:
            if term in term_frequency_dict:
                term_frequency_dict[term] += 1
            else:
                term_frequency_dict[term] = 1

    # print 30 most common words and their counts and add most common words to list
    sorted_termfrequency = sorted(term_frequency_dict.items(), key=lambda x: x[1], reverse=True)
    most_common = []
    print('\n30 most important words:')
    for i in range(30):
        print(sorted_termfrequency[i])
        most_common.append(sorted_termfrequency[i][0])

    # recipe, cake, flour, sugar, butter, egg, minutes, bowl, baking, batter
    # identified as top ten terms. Create a dict of these terms and sentences
    # in the files that use them.
    top_ten_words = ['recipe', 'cake', 'flour', 'sugar', 'butter', 'egg', 'minutes', 'bowl', 'baking', 'batter']
    file_no = 0
    while file_no < 15:
        # open file and tokenize the sentences
        file_no += 1
        file_to_read = "url" + str(file_no) + "sentences.txt"
        fd_read = open(file_to_read, 'r')
        text = fd_read.read()
        sentences = sent_tokenize(text)

        # check for keywords in the sentences in each file,
        # and add the sentence to the knowledge base dict if the
        # sentence contains a key word.
        for sentence in sentences:
            for word in top_ten_words:
                if word in sentence:
                    if word not in knowledge_dict:
                        knowledge_dict[word] = list()
                        knowledge_dict[word].append(sentence)
                    else:
                        knowledge_dict[word].append(sentence)

    # pickle the knowledge base
    pickle.dump(knowledge_dict, open('knowledge_base_dict.p', 'wb'))







