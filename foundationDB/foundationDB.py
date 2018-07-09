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

fdb.api_version(520)
db = fdb.open()

domain_index = fdb.Subspace(('domain-index',))
similarweb = fdb.Subspace(('similarweb',))

path = "/home/ubuntu/foundationDB/test"
files = os.listdir(path)
#print ('hello')
#print (files)

@fdb.transactional
def add_url(tr, url, date, pos):
    tr[fdb.Subspace((pos, ))[url]] = str.encode(date)

def store_file_domain_index(domain, create_date):
    add_url(db, domain, create_date, 'domain-index')

def read_file(filename):
    #print ("hello")
    csvFile = pd.read_csv("/home/ubuntu/foundationDB/test/" + filename, usecols = ['domain', 'create_date'])
    for i in range(0, len(csvFile)):
        store_file_domain_index(csvFile['domain'][i], str(csvFile['create_date'][i]))
        #print (i)
        value = str(db[fdb.Subspace(('domain-index', ))[csvFile['domain'][i]]])
        #print (csvFile['domain'][i])
        #print (value)        
    return csvFile

def read_head(filename):
    csvFile = pd.read_csv(filename)
    print (csvFile.head())

def multiple_processors(filename_list):
    #with Pool(1) as p:
        #p.map(read_file, filename_list)
    for i in range(0, len(files)):
        read_file(files[i])

def multiple(filename_list):
     with Pool(1) as p:
        print(p.map(read_file, filename_list))

if __name__ == '__main__':
    multiple_processors(files)
    '''csvFile = pd.read_csv("/home/ubuntu/foundationDB/test/" + "aaa.csv", usecols = ['domain', 'create_date'])
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
