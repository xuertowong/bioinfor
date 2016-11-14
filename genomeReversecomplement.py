from Bio.Seq import Seq
import sys
fasta = sys.argv[1] 
txt = open(fasta.split('.')[0]+'-.fasta','w')
genome = ''
for line in open(fasta):
    if line.startswith('>'):
        txt.write(line)
        
    else:
        genome = genome+line.strip()
genome = Seq(genome)
genome = genome.reverse_complement()    
txt.write(str(genome))
txt.close()