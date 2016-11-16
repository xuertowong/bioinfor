# -*- coding:utf-8 -*-

import sys

csvName = sys.argv[1]
fimoName = sys.argv[2]
name = []
strand = []
matchedSeq = []
name2 = []
proName = []
note = []
k = 0
fileName = fimoName.split('.')[0]
txt = open(fileName+'F.csv','w')
for line in open(fimoName):
    if line.startswith('1'):    
        name.append(line.split('\t')[1])
        strand.append(line.split('\t')[4])
        matchedSeq.append(line.split('\t')[8])
    else: continue
    
for line in open(csvName):
    name2.append(str(line.split(',')[0]))
    proName.append(str(line.split(',')[6]))
    note.append(str(line.split(',')[7]))

for i in range(len(name)):
    for j in range(len(name2)):
        if name[i] == name2[j]:
            txt.write(name[i]+','+strand[i]+','+matchedSeq[i].strip()+','+proName[j]+','+note[j])
txt.close()                                 