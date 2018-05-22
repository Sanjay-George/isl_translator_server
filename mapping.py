# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:41:06 2018

@author: my lenovo
"""
import pandas as pd
import numpy as np



def mapping(sentence):
#    sentence = "me born 196 a 1966"
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

#mapping("please no garbage use dustbin")
#
#mapping("me born 196 a 1966")
