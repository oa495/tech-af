import pandas as pd
import json
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
all = all.dropna(thresh=1)

documents = all['high_concept'].tolist()


# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in str(document).lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] > 1]
         for text in str(texts)]
# pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('dict/startups.dict')  # store the dictionary, for future reference
# print(dictionary)

# create corpus
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('corpus/startups.mm', corpus)  # store to disk, for later use
print(corpus)
