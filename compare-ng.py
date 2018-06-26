import pandas as pd
from gensim import corpora, models, similarities
import json
import logging
import codecs

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
pd.set_option("display.width", 120)

# open csv files
ng = pd.read_csv("african-countries/Angola.csv") # put the csv of whatever country
ng_data = ng[['name','product_desc']]
ng_data = ng_data.dropna()

# load Dictionary
dictionary = corpora.Dictionary.load('dict/startups.dict')
# load corpus
corpus = corpora.MmCorpus('corpus/startups.mm') # comes from the first tutorial, "From strings to vectors"

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=300)

# num_best says get top 5 that are similar, you can change it. 
index = similarities.MatrixSimilarity(lsi[corpus], num_best=5, num_features=len(dictionary), corpus_len=len(corpus)) # transform corpus to LSI space and index it
# index.save('corpus/startups.index')
# index = similarities.MatrixSimilarity.load('corpus/startups.mm.index')

f = codecs.open('data.json', encoding="ISO-8859-1")
results = json.load(f)

edges = []
for row in ng_data.itertuples():
	doc = (row[2]).decode('utf-8', 'ignore')
	vec_bow = dictionary.doc2bow(doc.lower().split())
	vec_lsi = lsi[vec_bow] # convert the query to LSI space
	sims = index[vec_lsi] # perform a similarity query against the corpus
	for sim in list(sims):
		edge = {}
		edge['source'] = row[1]
		edge['target'] = results[sim[0]] 
		edge['weight'] = sim[1]
		edges.append(edge)

print edges
with open('sim-data/ng-.json', 'w') as outfile:
    json.dump(edges, outfile, ensure_ascii=False)

