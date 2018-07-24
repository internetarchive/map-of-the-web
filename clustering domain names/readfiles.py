import csv
import pandas as pd
import os
import requests as req

path = "/Users/zhengyuecheng/Desktop/fea"

csvFile = pd.read_csv(path + "/" + "data.csv", usecols = ['domain'])

#print (csvFile['domain'][0])

def analysis(str, word_dic):
	res = req.get("http://web.archive.org/__wb/search/tagcloud?n=" + str + "&counters=1")
	word_list = res.text.split(',')
	length = len(word_list)
	if length == 0 or word_list[0] == "[":
		return None
	words = []
	for i in range(0, length):
		if i % 2 == 0:
			words.append(word_list[i])
		else:
			word_dic[word_list[i - 1]] = word_list[i]
	return word_dic
	#print (word_dic)

def dict2csv(dict, file):
	with open(file, 'w') as f:
		w = csv.writer(f)
		for key, value in dict.items():
			key = key.replace('[', '').replace('\"', '')
			value = value.replace(']', '')
			#print (key.replace('[', ''))
			w.writerow([key, value])
		#w.writerows(dict.items())

word_dic = dict()
analysis(csvFile['domain'][0], word_dic)
dict2csv(word_dic, path + "/" + "teee.csv")
Len = len(csvFile['domain'])
number = 0
empty = {}
for i in range(0, 5000):
	print (i)
	word_dic = analysis(csvFile['domain'][i], word_dic)
	#print (word_dic)
	if word_dic == None or word_dic == empty:
		number += 1
		print ("yyyyyyyyyyyyyyyyyyyyyyyyyy")
	else:
		dict2csv(word_dic, path + "/" + str(i) + ".csv")
		word_dic = dict()

print(number)

print ("finished.")
