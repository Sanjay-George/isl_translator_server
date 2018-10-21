import pandas as pd

dataset = pd.read_csv("./build/sheet.tsv", delimiter = '\t', quoting=3)

# input : randomized sheet
# create data.tsv and test.tsv 
# 20%