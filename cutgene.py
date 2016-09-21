import numpy as np
    
def cutGene(filename,genefile,file):
    gene = ''
    for line in open(genefile):
        if line.find('>') ==-1:
            gene = gene+line
        else:
            continue
    myfile = open(file,'w')
    start = np.zeros((len(filename),1))
    end = np.zeros((len(filename),1))
    for i in range(len(filename)):
        if filename[i][0] != '':
            start[i] = filename[i][1]
            end[i] = filename[i][2]
        else: continue
    length = len(start)
    for i in range(length):
        if start[i] != 0:
            a = start[i]; b = end[i]
            c = gene[int(a)-1:int(b)+1]
            myfile.write('>'+str(filename[i][0])+'\n')
            myfile.write(str(c)+'\n')    
        else:
            continue
    myfile.close()
    return 0
    
    
    