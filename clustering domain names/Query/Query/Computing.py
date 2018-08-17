#import nltk
#nltk.download('words')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import words
import re
from gensim import corpora, models, similarities
import csv
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import json

wordlist = set(words.words())
wordnet_lemmatizer = WordNetLemmatizer()

def max_match(text):
	pos2 = len(text)
	result = ''
	while len(text) > 0:       
		word = wordnet_lemmatizer.lemmatize(text[0:pos2])
		if word in wordlist:
			result = result + text[0:pos2] + ' '
			text = text[pos2:]
			pos2 = len(text)
		else:
			pos2 = pos2 - 1
	return result[0:-1]

#print(os.path.dirname(__file__))
path = os.path.dirname(__file__) + "/domains"
new_path = os.path.dirname(__file__) + "/wordsbag"
files = os.listdir(path)
data = os.listdir(new_path)
#print (files[0][:-4])

def extract_words(path, file_name):
	tokens = []
	csvFile = pd.read_csv(path + "/" + file_name, usecols = ['word', 'number'])
	Lenth = len(csvFile['word'])
	txt_file = open(new_path + "/" + file_name[:-4] + ".txt", 'w')
	for i in range (0, Lenth):
		string = csvFile['word'][i]
		#print (type(string))
		string = re.sub("[^A-Za-z ]", ' ', str(string))
		words = string.split(" ")
		while '' in words:
			words.remove('')
		#token = [max_match(word) for word in words]
		token = [word for word in words]
		tokens = tokens + token
		#txt_file.write(str(tokens))
		#print (tokens)
	#print (tokens)
	for tok in tokens:
		txt_file.write(tok + "\n")
	txt_file.close()

'''for i in range (0, len(files)):
	print (i)
	extract_words(path, files[i])'''

'''documents = ["universit de kinshasa demokratische republik kongo","oficjalna strona","Shipment of gold arrived in a truck"]

texts = [[word for word in document.lower().split()] for document in documents]
print (texts)

dictionary = corpora.Dictionary(texts)
print (dictionary.token2id)

corpus = [dictionary.doc2bow(text) for text in texts]
print (corpus)

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
	print (doc)
print ("    yyyyy     ")
print (tfidf.dfs)
print (tfidf.idfs)'''
#print (data[0])

def result_cluster(docres, index):
	return docres[index].tolist().index(max(docres[index]))


#print (len(data))
L = len(data)
corpus_list = []
corpus_dict = dict()
for i in range(0, L):
	with open(new_path + "/" + data[i]) as f:
		#corpus_name = "corpus" + str(i)
		#print (corpus_name)
		corpus_name = f.read()
		corpus_list.append(corpus_name)
		corpus_dict[data[i][:-4]] = corpus_name

#print (corpus_list[0])
#print (data[0][:-4])
#print (corpus_dict["accuweather.com"])

cntVector = CountVectorizer()
cntTf = cntVector.fit_transform(corpus_list)
#print (cntTf)
lda = LatentDirichletAllocation(n_topics = 10, learning_offset = 50., random_state = 0)
docres = lda.fit_transform(cntTf)

'''for i in range(0, L):
	cluster = result_cluster(docres, i)
	print (cluster)'''
storage = [[] for i in range(0, 11)]
dictionary = dict()
for i in range(0, L):
	cluster = result_cluster(docres, i)
	#print (cluster)
	for j in range(0, 11):
		if cluster == j:
			#print (data[i][:-4])
			#print (data[i][:-4])
			#print(j)
			#print(i)
			dictionary[data[i][:-4]] = j
			storage[j].append(data[i][:-4])

def similar_domains(domain_name):
	cluster_num = dictionary[domain_name]
	return storage[cluster_num]

string = "accuweather.com"
def output(string):
	out = []
	for i in range(0, len(similar_domains(string))):
		if similar_domains(string)[i] != string:
			out.append(similar_domains(string)[i])
	return out

#print(output(string))

documents = []
'''documents.append(corpus_list[0])
documents.append(corpus_list[1])'''
documents = corpus_list

def tf_idf(string):
	texts = [[word for word in corpus.lower().split('\n')] for corpus in documents]
	dictionary = corpora.Dictionary(texts,prune_at=2000000)
	corpus_model= [dictionary.doc2bow(test) for test in texts]
	#print (corpus_model)

	tfidf_model = models.TfidfModel(corpus_model)

	corpus_tfidf = tfidf_model[corpus_model]

	testword = corpus_dict[string]
	test_bow = dictionary.doc2bow([word for word in testword.lower().split('\n')])
	test_tfidf = tfidf_model[test_bow]
	#print (test_tfidf)

	index = similarities.MatrixSimilarity(corpus_tfidf) 
	sims = index[test_tfidf]  
	#print (sims)

	LL = len(sims)
	result = []
	for i in range(0, LL):
		result.append([sims[i], data[i][:-4]])

	return result
	#print (result)

result = tf_idf(string)

def score(elem):
	return elem[0]

print ("#########################################")

#print(result)

def present(result):
	result.sort(key = score, reverse = True)
	top_10 = dict()
	for i in range(1, 11):
		top_10[result[i][1]] = str(round(result[i][0] * 100, 2)) + "%"
	top_10 = json.dumps(top_10, indent = 1)
	return top_10

#print (present(result))



#print (string)
#print (output(string))
#print (docres[0])
#print (docres[0].tolist().index(max(docres[0])) + 1)

print ("finished.")
