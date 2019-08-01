#need to load blast, can do this using 
#need to load python 3

#module load ncbi-blast
#module load python/3.6.3

#then if you have the script saved as a .py
#python3.6 half_blast.py

import subprocess
import csv
import time

with open('test.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile))

for gene in data:
    with open('database_file', 'w') as database_file, open('query_file', 'w') as query_file, open('half_blast.out', 'a') as outfile:
        midpoint = int((int(gene[3]))/2)
        first_half = gene[2][:(midpoint+1)]
        second_half = gene[2][(int(gene[3])-midpoint):]
        database_file.write('>'+gene[0]+'\n'+first_half)
        database_file.close()
        query_file.write('>'+gene[0]+'\n'+second_half)
        query_file.close()
        subprocess.call(['makeblastdb', '-in', 'database_file', '-parse_seqids', '-title', '"half_blast"', '-dbtype', 'prot'])
        from subprocess import PIPE, run

        command = ['blastp', '-db', 'database_file', '-query', 'query_file', '-outfmt', '6', '-evalue', '100']
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        outfile.write(result.stdout)
        outfile.close()
