from nltk.stem import WordNetLemmatizer
from nltk.corpus import words
import re
from gensim import corpora, models, similarities
import csv
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

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

path = "/Users/zhengyuecheng/Desktop/domains"
new_path = "/Users/zhengyuecheng/Desktop/wordsbag"
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
	return docres[index].tolist().index(max(docres[index])) + 1


#print (len(data))
L = len(data)
corpus_list = []
for i in range(0, L):
	with open(new_path + "/" + data[i]) as f:
		corpus_name = "corpus" + str(i)
		#print (corpus_name)
		corpus_name = f.read()
		corpus_list.append(corpus_name)

#print (corpus_list[0])
cntVector = CountVectorizer()
cntTf = cntVector.fit_transform(corpus_list)
#print (cntTf)
lda = LatentDirichletAllocation(n_topics=10, learning_offset=50., random_state=0)
docres = lda.fit_transform(cntTf)

storage = [[] for i in range(1, 11)]
dictionary = dict()
for i in range(0, L):
    cluster = result_cluster(docres, i)
    #print (cluster)
    for j in range(1, 11):
        if cluster == j:
        	#print (data[i][:-4])
        	dictionary[data[i][:-4]] = j
        	storage[j].append(data[i][:-4])
        	
#print (storage[1])
#print (dictionary["accuweather.com"])

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

print(output(string))

#print (docres[0])
#print (docres[0].tolist().index(max(docres[0])) + 1)

print ("finished.")
