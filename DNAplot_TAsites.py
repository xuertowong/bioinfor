import pandas as pd
import numpy as np


def TAfinder(genome, tacsv, address):
    gene = ''
    for line in open(genome):
        gene = gene+line.strip()
    ta = pd.read_csv(tacsv)
    site = np.zeros((len(gene),1))
    for i in range(len(ta)):
        if ta['reads'][i] != 0:
            site[ta['sites'][i]] = ta['reads'][i]
    output = open(address,'w')
    for i in range(len(site)):
        output.write(str(int(site[i]))+'\n')
    output.close()
        
        