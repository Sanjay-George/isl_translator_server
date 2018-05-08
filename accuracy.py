# -*- coding: utf-8 -*-

#open tst.from  
#open tst.to
#
#open the other two too
#      
#check inference(tst.from) == tst.to # pred == actual????

from inference import inference
from rules import check_rules
import random 

english1 = []
sign1 = []
english2 = []
sign2 = []

test_acc = 0
dev_acc = 0

with open('data/tst2012.from') as f:
    for line in f:
        print(line)
        english1.append(line)
        
with open('data/tst2012.to') as f:
    for line in f:
        print(line)
        sign1.append(line)
        
correct = 0        
for j in range(100) :
    print(j)
    i = random.randint(0, 248)
    temp = inference(english1[i])
    index = temp['best_index']
    translation = temp['answers'][index]
#    translation = check_rules(english1[i], translation)
    print(translation, sign1[i])
#    print(len(translation), len(sign1[i]))
    if str(translation).replace(" ", "").strip() == str(sign1[i]).replace(" ", "").strip() :
        print("true")
        correct += 1
dev_acc = correct / 100 * 100


with open('data/tst2013.from') as f:
    for line in f:
        print(line)
        english2.append(line)
        
with open('data/tst2013.to') as f:
    for line in f:
        print(line)
        sign2.append(line)       
        
correct = 0        
for j in range(100) :
    print(j)
    i = random.randint(0, 248)
    temp = inference(english2[i])
    index = temp['best_index']
    translation = temp['answers'][index]
    translation = check_rules(english2[i], translation)
#    print(len(translation), len(sign1[i]))
    print(translation, sign2[i])
    if str(translation).replace(" ", "").strip() == str(sign2[i]).replace(" ", "").strip() :
        print("true")
        correct += 1
test_acc = correct / 100 * 100