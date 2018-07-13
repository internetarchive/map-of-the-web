import fdb
import csv
import pandas as pd
import os
import itertools
import random
import time
import json
from functools import partial
from multiprocessing import Pool

fdb.api_version(510)
db = fdb.open('fdb.cluster')

domain_index = fdb.Subspace(('domain-index',))
similarweb = fdb.Subspace(('similarweb',))

path = "/home/zcheng/foundationDB/Build/all"
files = os.listdir(path)
#print ('hello')
#print (files)

@fdb.transactional
def add_url(tr, url, date):
    #tr[fdb.Subspace((pos, ))[url]] = str.encode(date)
    tr[domain_index.pack((url,))] = str.encode(date)

@fdb.transactional
def read_file(tr, filename):
    csvFile = pd.read_csv("/home/zcheng/foundationDB/Build/all/" + filename, usecols = ['domain', 'create_date'])
    print (len(csvFile))
    for i in range(0, len(csvFile)):
        #print (i)
        #print(csvFile['domain'][i])
        #print(str(csvFile['create_date'][i]))
        add_url(tr, csvFile['domain'][i], str(csvFile['create_date'][i]))
        #value = str(db[fdb.Subspace(('domain-index', ))[csvFile['domain'][i]]])
        #print (csvFile['domain'][i])
        #print (value)

def read_head(filename):
    csvFile = pd.read_csv("/home/zcheng/foundationDB/Build/all/" + filename, usecols = ['domain', 'create_date'])
    print (csvFile.head())

def multiple_processors(filename_list):
    for i in range(163, len(files)):
        print (i)
        print (files[i])
        read_file(db, files[i])

def multiple(filename_list):
     with Pool(1) as p:
        print(p.map(read_file, filename_list))

if __name__ == '__main__':
    #read_file("/home/zcheng/foundationDB/test/ae.csv")
    multiple_processors(files)
    #multiple(files)
    '''csvFile = pd.read_csv("/home/zcheng/foundationDB/small/" + "aaa.csv", usecols = ['domain', 'create_date'])
    for i in range(0, len(csvFile) - 1):
        store_file_archive(csvFile['domain'][i], str(csvFile['create_date'][i]))
        print (i)'''
    print ("finished.")
    #active = True
    #while active:
    #    domain_name = input("Domain:\n")
    #    if domain_name == "quit":
     #       active = False
     #   else:
     #       value = db[fdb.Subspace(('archive', ))[domain_name]]
     #       print('internet archive, create date:' + bytes.decode(value))
