import numpy as np
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

# define the class to process the mix slogan + bukowski
# copied from 05_slogans_in_verse
import string

from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer

class text_processor:

    def __init__(self, remover_function=None, tokenizer_function=None,
                 cleaning_function=None, stemmer_function=None,
                     vectorizer_function = CountVectorizer()):
        self.remover = remover_function
        self.tokenizer = tokenizer_function
        self.cleaner = cleaning_function
        self.stemmer = stemmer_function
        self.vectorizer = vectorizer_function


        if remover_function == 'no_punctuation':
            self.remover = self.no_punctuation
        if tokenizer_function == 'tk_word':
            self.tokenizer = self.tk_word
        if not tokenizer_function:
            self.tokenizer = self.splitter
        if cleaning_function == 'lowstem':
            self.cleaner = self.lowstem

   # cleaning functions

    def lower(self,X):
        sentences = []
        for sentence in X:
            sentences.append(sentence.lower())
        return sentences


    def no_punctuation(self,X):
    # remove the punctuation
        pos = []
        for sentence in X:
            for punc in string.punctuation:
                sentence = sentence.replace(punc,'')
            pos.append(sentence)
        return pos

 # tokenizer functions

    def tk_word(self,X):
        vocabulary = []
        for x in X:
            vocabulary.append(word_tokenize(x))
        return vocabulary


    def splitter(self, text):
        """
        Default tokenizer that splits on spaces naively
        """
        return text.split(' ')

   # stemmer function


    def stem(self,X):
        stemmed = []
        for word in (X):
            stem_word = stemmer.stem(word)
            stemmed.append(stem_word)
        return stemmed




    # vectorizing function
    def vectorize(self, X):
        self.vectorizer.fit(X)
        self.columns=self.vectorizer.get_feature_names()
        return self.vectorizer.transform(X).toarray()


    def fit(self,X):
        clear_text = self.remover(X)
        print("clear_text after remover",clear_text)
        clear_text = self.lower(clear_text)
#        clear_text = self.stem(clear_text)
        self.matrix = self.vectorize(clear_text)


# Function to find verse associated to slogan copied from notebook
def generator(lesdonnees):
    nlp = text_processor(remover_function='no_punctuation',tokenizer_function = 'tk_word'
                    ,stemmer_function = PorterStemmer,
#                    vectorizer_function=TfidfVectorizer(min_df=0.3, max_df=0.8))
                    vectorizer_function=TfidfVectorizer(min_df=0, max_df=1))

    df = pd.read_excel('bukowski1.xlsx')
    X = df['verses']
    pos = [lesdonnees][0]   # looks like nothing but the entry format of web form is not the same as NB
    for x in X:
        for punc in string.punctuation:
            x = x.replace(punc,'')
        pos.append(x)
    nlp.fit(pos)
    pos_matrix = nlp.matrix
    pos_columns = nlp.columns
    lsa = TruncatedSVD(2, algorithm = 'arpack')
    dtm_lsa = lsa.fit_transform(pos_matrix)
    dtm_lsa = Normalizer(copy=False).fit_transform(dtm_lsa)
    pd.DataFrame(lsa.components_.round(5),
                 index = ["component_1","component_2"],columns = pos_columns)
    df3 = pd.DataFrame(dtm_lsa.round(5), index = pos, columns = ["component_1","component_2" ])
    df4 = df3.nlargest(len(df3), 'component_1')
    df4 = df4.reset_index()
    mask1 = (df4['index'] == lesdonnees[0])
    print("string to get",df4[mask1])
    n = df4[mask1].index[0]
    df5 = df3.nlargest(len(df3), 'component_2')
    df5 = df5.reset_index()
    mask5 = (df5['index'] == lesdonnees[0])
    m = df5[mask5].index[0]

    return (lesdonnees[0]+' .... '+df4.iloc[n+1]['index']) 
    # RETURNS initial slogans and found verse
