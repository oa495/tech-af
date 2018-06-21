import pandas as pd
import json
import re
from gensim import corpora
from collections import defaultdict
from pprint import pprint  # pretty-printer

pd.set_option("display.width", 120)
# open csv file
ng = pd.read_csv("african-countries/Nigeria.csv")
us_1 = pd.read_csv("us/us1.csv")
us_2 = pd.read_csv("us/us2.csv")
frames = [us_1, us_2, ng]
all = pd.concat(frames)

def remove_chars(string):
	string = re.sub(r"([^\s\w]|_)+", "", str(string))
	return string

documents = (all['product_desc'].apply(remove_chars)).tolist()

# TODO: If product_desc empty replace with high_concept

documents = list(filter(lambda item: (item != ' ' and item != 'nan'), documents))

# TODO: add more stop words

# remove common words and tokenize
stoplist = set('for a of the and to in nigeria africans africa'.split())
texts = [[word for word in str(document).lower().split() if word not in stoplist]
         for document in documents]

# pprint(texts)

# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('dict/startups.dict')  # store the dictionary, for future reference

# create corpus
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('corpus/startups.mm', corpus)  # store to disk, for later use