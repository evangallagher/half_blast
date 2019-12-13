#!/bin/bash
pwd; hostname; date

module load python/3.6.3
module load ncbi-blast
module load NcbiblastxCommandline

python local_half_blast.py

done
