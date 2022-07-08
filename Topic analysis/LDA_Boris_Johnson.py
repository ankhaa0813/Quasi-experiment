import json
import numpy
import pandas as pd
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import pyLDAvis
import pyLDAvis.gensim_models
#I will implement simple topic analysis to estimate the public opinion about the Boris Johson in twitter using tweets about him. 
# I downloaded the 10 thousand tweets which is tweeted in last week and contained key word Boris Johson through Twarc library. 
# I prepared overview of LDA, common topic analysis' technique in the readme file.

data=pd.read_csv('boris_tweets.csv')
data.head
#Extracting only tweet texts from full dataset which contain all meta datas about twitter
lda_data=data['text']
data.columns # see the columns of the table 
lda_data.head

from nltk.corpus import stopwords #downloading pre-defined stopwords
stop_words = stopwords.words('english')
#Adding some words to stopwords such as key terms and some words that don't contain any information. for example in tweets corpus which is collected with key terms about goettingen
# Since key terms are in every tweet, we can't make any conclusion from that
stop_words.extend(['boris','johnson', 'minister','https'])  #additional
from gensim.utils import simple_preprocess
#Defining a new function which is going to be used to transform dataset
# deacc=True removes punctuations
def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
#Defining a new function which is going to be used later to remove stopwords
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]
#creating new list that contains only the elements that satisfies if condition or not in list of stopwords.
# and it does for each tweets in the corpus called texts (generally speaking it is called documents)
# word in word function is the way to create lists where each element is the result of some operations 
# applied to each member of another seqeunce.
# In particular, we are creating subsequency of those elements that satisfy a certain condition. 
# Now we are using functions which is defined previously 
data_words = list(sent_to_words(lda_data)) #transform data set word by word 
# printing 
print(data_words[:1][0][:30])
data_words = remove_stopwords(data_words) # removing stopwords
print(data_words[:1][0][:30])

import gensim.corpora as corpora
#Donwloading data and creating bag of words which is list of unique words and their frequency 
id2word = corpora.Dictionary(data_words)
# Create Corpus
texts = data_words
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
#information saved in corpus is the exact same information in data_words variable
print(corpus[0][:10])
word_example= id2word[1][:1][0]
print(word_example)
# 0 corresponds to index of the words and their frequency 
# defining number of topics number of topics
num_topics = 20 # Number of topics are quite arbitrary. But you can experiment several option and choose the one with better performance
# Build LDA model
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics)
# Print the Keyword in the 10 topics
print(lda_model.print_topics())
doc_lda = lda_model[corpus]
#pyLDAvis command shows the estimated topics with its frequency as comparing simple PCA results
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds="mmds", R=30)
pyLDAvis.save_html(vis, 'LDA_Visualization.html')