# Library of tokenizer functions

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

def tkword(my_text):
    return word_tokenize(my_text)

'''
separate the words find the spaces

ex:INPUT
my_text = "Hi Mr. Smith! I’m going to buy some vegetables (tomatoes and cucumbers)
from the store. Should I pick up some black-eyed peas as well?"
OUTPUT:
['Hi', 'Mr.', 'Smith', '!', 'I', '’', 'm', ‘going', ‘to', 'buy', 'some', 'vegetables',
 '(', 'tomatoes', 'and', 'cucumbers', ')', 'from', 'the', 'store', '.', 'Should',
 'I', 'pick', 'up', ‘some', 'black-eyed', 'peas', 'as', 'well', '?']
 '''


def tksentence(my_text):
    return sent_tokenize(my_text)

'''
separate the sentences find the punctuation

ex:INPUT
my_text = "Hi Mr. Smith! I’m going to buy some vegetables (tomatoes and cucumbers)
from the store. Should I pick up some black-eyed peas as well?"
OUTPUT: found . and creates an item in the list for each sentence
['Hi Mr. Smith!',
'I’m going to buy some vegetables (tomatoes and cucumbers) from the store.',
 'Should I pick up some black-eyed peas as well?']
 '''

def tkngram(my_text,n):
    my_words = word_tokenize(my_text)
    grams = list(ngrams(my_words,n))
    return grams
'''
create tuple of words
ex:INPUT
my_text = "Hi Mr. Smith! I’m going to buy some vegetables (tomatoes and cucumbers)
from the store. Should I pick up some black-eyed peas as well?"
n=2
[('Hi', 'Mr.'), ('Mr.', 'Smith'), ('Smith', '!'), ('!', 'I'), ('I', '’'),
('’', 'm'), ('m', 'going'), ('going', 'to'), ('to', ‘buy'), ('buy', 'some'),
('some', 'vegetables'), ('vegetables', '('), ('(', 'tomatoes'),
('tomatoes', 'and'), ('and', 'cucumbers'),
('cucumbers', ')'), (')', 'from'), ('from', 'the'), ('the', 'store'),
 ('store', '.'), ('.', 'Should'), ('Should', 'I'), ('I', 'pick'),
 ('pick', 'up'), ('up', '1/2'), ('1/2', 'lb'), ('lb', 'of'),
 ('of', 'black-eyed'), ('black-eyed', 'peas'), ('peas', 'as'), ('as', 'well'),
  ('well', '?')]
'''


def tkspace(my_text):
     operator  = RegexpTokenizer("\s+", gaps=True)
     return operator.tokenize(my_text)
