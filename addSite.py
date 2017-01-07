import os
import sys
import pandas as pd

inputfile = sys.argv[1]
sitename = sys.argv[2]
b = pd.read_csv(sitename)
for filename in os.listdir(inputfile):
    a = pd.read_csv(inputfile+'\\'+filename)
    c = pd.merge(a, b, on='name', how='left')
    c.to_csv(filename.split('.')[0] + 'output'+'.csv')
    