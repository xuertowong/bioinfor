import numpy as np
import os 
import sys

addr = 'D:\yz2'
chromTA = 'D:\TA2.txt'
filename = os.listdir(addr)
for i in range(len(filename)):
    name = filename[i].split('.')
    name = name[-2]
    a = []
    for line in open(chromTA).readlines():
        line = line.strip()
        a.append(line)
    b = []
    n = addr+'\\'+filename[i]  
    for line in open(n).readlines():
        line = line.strip()
        b.append(line)
    
    a = np.array(a)
    a.astype(float)
    b = np.array(b)
    b.astype(float)
    c = open(str(addr+'\\'+name+'.wig'),'w')
    for i in range(len(a)):
        c.write(a[i]+' '+b[i]+'\n')
    
    c.close()
    