import pandas as pd
import numpy as np
import os
import sys

address1 = sys.argv[1]
address2 = sys.argv[2]
fileName = address1.split('.')[0] + 'output.csv'
tafile = pd.read_csv(address1)
chrfile = pd.read_csv(address2)

tasite = list(tafile['tasite'])
tanums = list(tafile['num'])
start = list(chrfile['start'])
end = list(chrfile['end'])

def length(x, y):
    length = abs(y - x) * 0.1
    x = x + length
    y = y - length
    return x,y
    
c = np.zeros((np.shape(start)))
startend= list(map(length, start, end))
startend = list(map(list, startend))

for i in range(len(tanums)):
    if tanums[i] > 0:
        for j in range(len(start)):
            if tasite[i] > startend[j][0] and tasite[i] < startend[j][1]:
                c[j] = c[j] + tanums[i]
    else:
        continue
                
e = pd.DataFrame(c)
e.to_csv(fileName)
