# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:41:06 2018

@author: my lenovo
"""
import pandas as pd
import numpy as np

#sentence = 'where you go'
#sentence  = sentence.split(" ")
#sign = []
#
#for word in sentence:
#    index = dataset.index[dataset['english'] == word].tolist()
#    index = index[0]
#    print(index)
#    sign.append(dataset['sign'][index])
#    
#
#sign = " ".join(sign)

def mapping(sentence):
    dataset = pd.read_csv("mapping.tsv", delimiter = '\t', quoting=3)
    sentence  = sentence.split(" ")
    sign = []
    for word in sentence:
        index = dataset.index[dataset['word'] == word].tolist()
        index = index[0]
#        print(index)
        sign.append(dataset['mapping'][index])
    sign = " ".join(sign)
#    print(sign)
    return sign

mapping("please no garbage use dustbin")