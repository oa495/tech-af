import sys
import pandas as pd
import json
import re
from gensim import corpora
from collections import defaultdict
from pprint import pprint  # pretty-printer

pd.set_option("display.width", 120)
# open csv file
us_1 = pd.read_csv("countries/us1.csv")
us_2 = pd.read_csv("countries/us2.csv")
frames = [us_1, us_2]
us = (pd.concat(frames)).drop_duplicates().reset_index(drop=True)
us = us.dropna()

def remove_chars(string):
	string = re.sub(r"([^\s\w]|_)+", "", str(string))
	return string

names = us['name'].tolist()
documents = (us['product_desc'].apply(remove_chars)).tolist()

# TODO: If product_desc empty replace with high_concept

tuples = [(names[i], documents[i]) for i in xrange(len(documents))]
tuples = list(filter(lambda item: (item[1] != ' ' and item[1] != 'nan'), tuples))
names = [t[0] for t in tuples]
documents = [t[1] for t in tuples]

# TODO: add more stop words

# remove common words and tokenize
stoplist = set('for a of the and to in nigeria africans africa'.split())
texts = [[word for word in str(document).lower().split() if word not in stoplist]
         for document in documents]


with open('data.json', 'w') as outfile:
    json.dump(names, outfile, ensure_ascii=False)


# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save('dict/startups.dict')  # store the dictionary, for future reference

# create corpus
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('corpus/startups.mm', corpus)  # store to disk, for later use
