from Bio.Seq import Seq

def genomeReverse(fasta): 
    savefileName = fasta.split('.')[0]
    txt = open(savefileName+'-.fasta','w')
    for line in open(fasta):
        if line.startswith('>'):
            txt.write(line+'\n')
            genome = ''
        else:
            genome = genome+line.strip()
    genome = Seq(genome)
    genome = genome.reverse_complement()    
    txt.write(str(genome))
    txt.close()