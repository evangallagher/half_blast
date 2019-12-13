from Bio.Blast.Applications import NcbiblastxCommandline


openthisfile = 'example_multifasta.fa'
writetothisfile = 'multifasta.txt'
data = []
sequence = None
seq_len = 0
gene_count = 0

with open(openthisfile, 'r') as fastafile:
        for line in fastafile:
            if '>' in line:
                gene_count += 1
                if sequence is not None:
                    seq_len = len(sequence)
                    protein.append(sequence)
                    protein.append(seq_len)
                    sequence = None
                    data.append(protein)
                protein = []
                protein.append(line.rstrip('\n'),)
            elif (len(line) != 0) and (sequence is not None):
                sequence += (line.rstrip('\n'))
            elif (len(line) != 0) and (sequence is None):
                sequence = (line.rstrip('\n'))
seq_len = len(sequence)
protein.append(sequence)
protein.append(seq_len)
data.append(protein)

with open(writetothisfile, 'a') as outfile:
    outfile.write('Half Blast of: '+openthisfile+' Contains: '+str(gene_count)+' proteins'+'\n'+'query acc.ver, protein length, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score'+'\n')
    outfile.close()
    fastafile.close()

for gene in data:
    with open('database_file', 'w') as database_file, open('query_file', 'w') as query_file, open(writetothisfile, 'a') as outfile:
        midpoint = int((int(gene[2]))/2)
        first_half = gene[1][:(midpoint+1)]
        second_half = gene[1][(int(gene[2])-midpoint):]
        database_file.write('>'+str(gene[2])+'\n'+first_half)
        database_file.close()
        query_file.write(gene[0]+'\n'+second_half)
        query_file.close()

        blastx_command = NcbiblastxCommandline(query="query_file", db="database_file", evalue=0.001, outfmt=5, out="multifast.txt")
        blastx_command
        outfile.write(results.read())
        outfile.close()
