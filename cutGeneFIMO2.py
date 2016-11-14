import numpy as np
import sys
from matplotlib.mlab import csv2rec

filename = sys.argv[1]
genefile = sys.argv[2]
num = sys.argv[3]
csv = csv2rec(filename)
gene = ''
for line in open(genefile):
    if line.find('>') ==-1:
        gene = gene+line.strip()
    else:
        continue
myfile = open(filename.split('.')[0]+'.txt','w')
start = np.zeros((len(csv),1))
end = np.zeros((len(csv),1))
for i in range(len(csv)):
    if '-' in filename:
        start[i] = csv[i][2]
        end[i] = csv[i][2] + int(num)
    if '+' in filename:
        start[i] = csv[i][1] - int(num)
        end[i] = csv[i][1]
    else: continue
length = len(start)
for i in range(length):
    if start[i] != 0:
        a = start[i]; b = end[i]
        c = gene[int(a)-1:int(b)]
        myfile.write('>'+str(csv[i][0])+'\n')
        myfile.write(str(c)+'\n')    
    else:
            continue
myfile.close()

    
    
    