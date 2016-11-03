#!/usr/env/bin python
# -*- coding:utf-8 -*-
import os
import sys

gff = sys.argv[1]
saveFile = sys.argv[2]
fileName = saveFile.split('.')[0]
txt = open(saveFile, 'w')
annotation = open(gff)
for line in annotation:
    if line.startswith('#'):
        continue
    tmp = line.strip().split('\t')
    chr = tmp[0]
    type = tmp[2]
    start = int(tmp[3])
    end = int(tmp[4])
    strand = tmp[6]
    features = dict([tuple(f.split("=")) for f in tmp[8].split(";")])
    name = features.get('Name')
    if name == '1':
        txt.write('Chromesome1\n'+'Name,'+'Start,'+'End,'+'Chr,'+'Type'+'\n')
    elif name == '2':
        txt.write('Chromesome2\n'+'Name,'+'Start,'+'End,'+'Chr,'+'Type'+'\n')  
    else:             
        txt.write(str(name)+','+str(start)+','+str(end)+','+str(chr)+'\t'+str(strand)+','+str(type)+'\n')
txt.close()
os.rename(saveFile,str(fileName)+'.csv')
           
            