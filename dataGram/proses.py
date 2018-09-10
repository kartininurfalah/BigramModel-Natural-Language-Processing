# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:31:29 2018

@author: kartini
"""

import numpy as np
import pandas as pd
import re
import nltk
import collections
from nltk import bigrams
import math

dataArtikel = pd.read_csv('/media/kartini/Kuliah/KULIAH/Semester 7/NLP/news/artikel.csv')
dataTrainArtikel = pd.read_csv('/media/kartini/Kuliah/KULIAH/Semester 7/NLP/news/artikelTrain.csv')

#arrArticles = dataArtikel

arrArticle = dataTrainArtikel['article']

#merge artikel
articles = ' '.join(arrArticle)

bow = []

#word tokenize, delete stop word , and lower
subTandaBacaArtikel = re.sub('[–"!@#$%()&+,./;:=“”\'0123456789‘-]', '', articles)
bow = (subTandaBacaArtikel.lower().split())

uniqueBOW = np.unique(bow)
wordUnique_counter = collections.Counter(bow)

bigramMatriks = np.zeros((len(uniqueBOW), len(uniqueBOW)), dtype = int)

for i, artikel in enumerate(bow):
    if (i == len(bow)-1):
        break
    for j, row in enumerate(uniqueBOW):
        for k, column in enumerate(uniqueBOW):
            if (artikel != row):
                break
            if (artikel == row) and (bow[i+1] == column):
                bigramMatriks[j][k] +=1

#smoothing
bigramMatriks[bigramMatriks >= 0] += 1

bigramProbabilities = np.zeros((len(uniqueBOW), len(uniqueBOW)))

for i, row in enumerate(bigramMatriks):
   # print(i)
    for j, columnCount in enumerate(row):
        bigramProbabilities[i][j] = columnCount/ (wordUnique_counter[uniqueBOW[i]] + len(uniqueBOW))
        #print(wordUnique_counter['ada'])
        
#sentences = 'Seekor anak Asia milik Kebun Binatang'.lower().split()   
sentences = 'seekor anak asia kebun milik Binatang'.lower().split()

#compute sum of log
soLog = 0
for i, kata in enumerate(sentences):
    if (i == len(sentences) - 1):
        break
    indeksKata1 = uniqueBOW.tolist().index(kata)
    indeksKata2 = uniqueBOW.tolist().index(sentences[i + 1])
    
    probabilitas = bigramProbabilities[indeksKata1, indeksKata2]
    logProb = math.log2(probabilitas)
    
    soLog += logProb

print('Sum of Log: ',soLog)

#compute L = 1/M * sumoflog, M = sumof sentences
l = 1/len(sentences) * soLog

#compute perplexity = 2^-l
perplexity = math.pow(2, -1 * l)

print('Perplexity: ', perplexity)
    
pd.DataFrame(bigramProbabilities).to_csv('Bigram-Probabilities-smoothing.csv', index=False, header=False)
pd.DataFrame(uniqueBOW).to_csv('BagOfWords-update.csv', index=False, header=False)