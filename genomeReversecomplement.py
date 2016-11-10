from Bio.Seq import Seq

def genomeReverse(fasta,savefile):
    genome = ''
    for line in open(fasta):
        genome = genome+line.strip()
    genome = Seq(genome)
    genome = genome.reverse_complement()
    txt = open(savefile,'w')
    txt.write(str(genome))
    txt.close()