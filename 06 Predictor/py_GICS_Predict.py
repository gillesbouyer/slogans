import pickle
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import porter
from nltk.tokenize import word_tokenize
import string
stemmer = porter.PorterStemmer()
stopwords = stopwords.words()

# read in the model and the words
lr= pickle.load(open("slogpred.p","rb")) # the model
columns= pickle.load(open("colonnes.p","rb")) # the list of my_words
# we calculate a word vector with same columns as list of words
# cleanup function - same as in predictor notebook
def clean_text(text):
    cleaned_text = []
    for post in text:
        cleaned_words = []
        post = post.replace("’",'')
        for punc in string.punctuation:
            post = post.replace(punc,'')
        for word in post.split():
            low_word = stemmer.stem(word.lower())
            if low_word not in stopwords:
                cleaned_words.append(low_word)
        cleaned_text.append(' '.join(cleaned_words))
    return cleaned_text


# Use the same cleaning function than the one for the model

def predictcigs(lesdonnees):
    text_propre = clean_text(lesdonnees)
    S = word_tokenize((text_propre)[0])
    VS = np.zeros((1,len(columns))) # initialize and fill a 0/1 vector for the slogan
    for a in S:
        if a in columns:
            j = columns.index(a)
            print("j",j)
            VS[0,j] = VS[0,j] + 1
    print(lr.predict(VS)) # vector of number of words
    prediction = lr.predict(VS).mean()
    prediction = int(prediction)-1 # INDEX STARTS AT 0

    # return a message indexed on the value returned
    # built with classes 1 to 11 in previous notebook
    message_array = ["You are likely a consumer product company !",
    "You are likely a Food and Beverage company !",
    "You are likely an Energy company !",
    "You are likely a Financial company !",
    "You are likely an Industrial company !",
    "You are likely a healthcare company ! ",
    "You are likely an IT company",
    "You are likely raw material company ",
    "You are likely a real estate company",
    "You are likely a Telecom company",
    "You are likely a Utility company",]

    return message_array[prediction]
