# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 13:47:29 2018

@author: kartini
"""

import numpy as np
import pandas as pd


dataBigramProbabilities = pd.read_csv('/media/kartini/Kuliah/KULIAH/Semester 7/NLP/dataGram/Bigram-Probabilities.csv', header=None).values.tolist()
dataBagOfWords = pd.read_csv('/media/kartini/Kuliah/KULIAH/Semester 7/NLP/dataGram/BagOfWords.csv', names=['words'])['words'].tolist()

inputWord = ''

while (inputWord != '3'):
    
    inputWord = input('Masukkan Kata: ')
    if inputWord in dataBagOfWords:
        #print('ditemukan')
        indeksKata = dataBagOfWords.index(inputWord)
        maxProbabilities = np.max(dataBigramProbabilities[indeksKata])
        indeks = dataBigramProbabilities[indeksKata].index(maxProbabilities)
        print('Output next kata: ',dataBagOfWords[indeks])
       # print
    else:
        print('Kata tidak ditemukan!')