# rules for translation 
# helps to translate better for smaller datasets
# DO THIS AFTER FINAL TRAINING


#RULES : 
#1. MONTHS, days
#2. NUMBERS
#3. NAMES...
#4. IF LEN(SIGNS) > LEN(WORDS) : MATCH AND SPELL
import pandas as pd

months = ['januari', 'februari', 'march', 'april', 'may', 'june', 'juli', 'august', 'septemb', 'octob', 'novemb', 'decemb'] 
months_sign = ["j eid", "f ", "m march", "a blank a", "m a y", "j rain", "j y ", "a tiewrist", "s blank s ", "october", "n cracker", "d cold"]
days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]



# ---------------------------
# RULE BASED TRANSLATION CODE
# ---------------------------
# RULES FOR MONTHS
def month_rules(english, sentence):
    english = english.split()
    sign = ''
    sign = sentence + ' '
    # loop 1 : check if months present, else exit
    m_indices = []
    for word in english:
        if word in months:
            m_indices.append(months.index(word))
    if len(m_indices) == 0 :
#        print("no months exist. RETURN from function")
        return sentence # EXIT IF NO MONTHS IN THE SENTENCE
    
    # loop 2 : find indices of months in the signs
    s_indices = {}
    for month in months_sign:
        index = sign.find(month)
        if index > -1:
            s_indices[index] = month
    # sort the dict
    import operator
    sorted_indices = sorted(s_indices.items(), key = operator.itemgetter(0))
    s_indices = dict(sorted_indices)
    # loop 3 : replace the months in sign
    i = 0 
    for key in s_indices:
        index = m_indices[i]
        i += 1
        sign = sign.replace(s_indices[key], months_sign[index])
    sentence = sign.rstrip()
#    print(sentence)
    return sentence
    

#-------------------------------------------        
# RULES FOR NUMBERS ( YEARS, DATES, ETC)
def number_rules(english, sentence):
    english = english.split()
    sign = sentence.split()
    indices = []
    # find pos of numbers in english  LOOP 1
    for word in english:
        if word.isdigit():
            indices.append(english.index(word))
#    print(indices)
    if len(indices) == 0:
        return sentence # EXIT IF NO NUMBERS IN THE SENTENCE
    i = 0
    # replace corres numbers in sign  LOOP 2
    for word in sign:
        if word.isdigit():
            sign[sign.index(word)] = english[indices[i]]
            i += 1
#    print(sign) 
    # add spaces between numbers     LOOP 3
    for i in range(len(sign)):
        if sign[i].isdigit():
            number = sign[i]
            temp = ''
            for ch in number:
                temp = temp + ch + ' '  
            sign[i] = temp.rstrip()
            
    sentence = " ".join(sign) # final result, return this
#    print(sentence)
    return sentence

#----------------------------------------
# RULES FOR NAMES
def name_rules(english, sentence): 
    not_names = ["what", 'your' , "i", "my", "her", "hi", "is", "was", "name", "goes", "by", "the", "known", "as", "you", "can", "call", "me"]
    english = english.split()
    sign = sentence.split()
    # loop 1 : find index of the start of name in sign sentence
    start_index = 0
    for i in range(len(sign)):
        if sign[i] == "name" and sign[i+1] not in not_names:
            start_index = i + 1
    if start_index == 0:
        return sentence # EXIT IF NO NAMES IN THE SENTENCE
    # set real name from english        
    real_name = [word for word in english if not word in set(not_names)]
    j = 0
    # looop 2 : set real name into sign and separate by spaces
    for i in range(start_index, len(sign)):
        if j == len(real_name):
            break
        name = real_name[j]
        j += 1
        temp = ''
        for ch in name:
            temp = temp + ch + ' '
        sign[i] = temp.rstrip()
    
    for i in range(j + start_index, len(sign)):
        sign[i] = ''
    
    sentence = " ".join(sign)
#    print(sentence)
    return sentence


# GENERIC RULES FOR NAMES : ADD LATER IF NEEDED 

#def names_rules_generic(english, sentence):
#english = "she talked to rahul"
#sentence = 'she talk j o h n'
    
#names = pd.read_csv("resources/data/indian_names/names.tsv", delimiter = '\t', quoting = 3)
#names = names.iloc[:, 0].values
#names = [name.lower() for name in names]
    
#english = english.split()
#sign = ''
#sign = sentence + ' '
## loop 1 : check if names present, else exit
#n_indices = []
#for word in english:
#    if word in names:
#        n_indices.append(names.index(word))
#if len(n_indices) == 0 :
#    print("no names exist. RETURN from function")
##    return sentence # EXIT IF NO MONTHS IN THE SENTENCE
#
## loop 2 : find indices of months  in the signs
#s_indices = {}
#for month in months_sign:
#    index = sign.find(month)
#    if index > -1:
#        s_indices[index] = month
## sort the dict
#import operator
#sorted_indices = sorted(s_indices.items(), key = operator.itemgetter(0))
#s_indices = dict(sorted_indices)
## loop 3 : replace the months in sign
#i = 0 
#for key in s_indices:
#    index = m_indices[i]
#    i += 1
#    sign = sign.replace(s_indices[key], months_sign[index])
#sentence = sign.rstrip()
#print(sentence)
##return sentence   
#
#




# CALLING FUNCTION
def check_rules(english, sentence):    
    sentence = month_rules(english, sentence)
    sentence = number_rules(english, sentence)
    sentence = name_rules(english, sentence)
    sentence = sentence.rstrip()
    return sentence

#print(check_rules("she 16 died", "she died 16"))

