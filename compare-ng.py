import pandas as pd
from gensim import corpora, models, similarities
import json
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
pd.set_option("display.width", 120)

# open csv files
ng = pd.read_csv("countries/Nigeria.csv")
us_1 = pd.read_csv("countries/us1.csv")
us_2 = pd.read_csv("countries/us2.csv")
frames = [us_1, us_2]
us = pd.concat(frames)

# load Dictionary
dictionary = corpora.Dictionary.load('dict/startups.dict')
# load corpus
corpus = corpora.MmCorpus('corpus/startups.mm') # comes from the first tutorial, "From strings to vectors"

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=300)

index = similarities.MatrixSimilarity(lsi[corpus], num_best=5, num_features=len(dictionary), corpus_len=len(corpus)) # transform corpus to LSI space and index it
index.save('corpus/startups.index')
index = similarities.MatrixSimilarity.load('corpus/startups.mm.index')

ng_list = ng['product_desc'].tolist()

for doc in ng_list:
	vec_bow = dictionary.doc2bow(doc.lower().split())
	vec_lsi = lsi[vec_bow] # convert the query to LSI space

	sims = index[vec_lsi] # perform a similarity query against the corpus
	print(list(enumerate(sims))) # print (document_number, document_similarity) 2-tuples
