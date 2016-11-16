#!/usr/env/bin python
# -*- coding:utf-8 -*-
import os
import sys
'''This is script for converting the .gff format into .csv format.
The .csv format can present the infomation of each gene clearly.
The output file includes the chromesome information and each gene sites' start point, end point, strand,name,type,chromesome.
'''             
gff = sys.argv[1]
saveFile = sys.argv[2]
fileName = saveFile.split('.')[0]
txt = open(saveFile,'w')
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
    note = features.get('Note')
    none = 'NaN'
    bioType = features.get('gene_biotype')
    gbkey = features.get('gbkey')
    ID = features.get('ID')
    if bioType == 'protein_coding'  :
        temp = name
        continue
    if gbkey == 'repeat_region' or gbkey =='misc_binding'or bioType =='pseudogene':
        temp = ID
        continue
    if 'RNA' in str(bioType):
        temp = bioType
        txt.write(str(name)+','+str(start)+','+str(end)+','+'Chromesome'+str(a)+','+str(strand)+','+str(type)+','+str(bioType)+','+str(note)+'\n')
        continue
    if 'RNA' in str(gbkey):
        continue
    else:
        if str(name).isdigit():    
            txt.write('Genename,'+'Start,'+'End,'+'Chr,'+'Strand,'+'Type,'+'proName/tRNA,'+'Note\n')
            a = name
        else:  
            txt.write(str(temp)+','+str(start)+','+str(end)+','+'Chromesome'+str(a)+','+str(strand)+','+str(type)+','+str(name)+','+str(note)+'\n')
txt.close()
os.rename(saveFile,fileName+'.csv')

txt = open(fileName+'.csv')
i = 1
for line in txt.readlines():
    if line.startswith('Genename'):
        chrF = open(fileName+str(i)+'+.csv','w')
        chrR = open(fileName+str(i)+'-.csv','w')
        chrF.write(line)
        chrR.write(line)
        i = i+1
    else:
        tmp = line.strip().split(',')
        if tmp[4] == '-':
            chrR.write(line)
        if tmp[4] == '+':
            chrF.write(line)
            


