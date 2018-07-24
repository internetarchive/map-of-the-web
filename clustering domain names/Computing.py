from nltk.stem import WordNetLemmatizer
from nltk.corpus import words
import re
from gensim import corpora, models, similarities

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

string = "universit de kinshasa demokratische republik kongo"
#string = re.sub(r'\\u+', ' ', string)
words = string.split(" ")

tokens = [max_match(word) for word in words]

print (tokens)

documents = ["universit de kinshasa demokratische republik kongo","oficjalna strona","Shipment of gold arrived in a truck"]

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
print (tfidf.idfs)
