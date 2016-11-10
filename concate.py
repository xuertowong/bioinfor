import pandas as pd
import numpy as np
from pandas import DataFrame
import sys

a = sys.argv[0]
saveFile = sys.argv[1]
fileName = a.split('.')[0]
address = sys.argv[2]
a = pd.read_csv(a)
c = a.columns
b = np.array(a)
for i in range(len(b)-2):
    if b[i][1] == b[i+1][1] and b[i+1][5] != 'tRNA' and  b[i+1][5] != 'exon':
        b[i][7] = b[i+1][0]
        b[i][6] = b[i+1][6]
    elif b[i][1] == b[i+1][1] and b[i+1][5] == 'tRNA':
        b[i][6] = b[i+1][6]
        b[i][7] = b[i+1][5]
        b[i][8] = b[i+2][5]
    elif b[i][1] == b[i+1][1] and b[i+1][5] == 'exon':
        continue
    else:
        continue
a = DataFrame(b,columns=c)
a = a[a['CDS/tRNA'].notnull()]

a.to_csv(address)