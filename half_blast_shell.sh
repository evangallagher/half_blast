#!/bin/bash
#SBATCH -p short # Partition or queue. In this case, short!
#SBATCH --job-name=half_blast # Job name
#SBATCH --mail-type=END # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=shla9937@colorado.edu
#SBATCH --nodes=1 # Only use a single node
#SBATCH --ntasks=1 # Run on a single node
#SBATCH --cpus-per-task=60 # cpus
#SBATCH --mem=400gb # Memory limit
#SBATCH --time=12:00:00 # Time limit hrs:min:sec
#SBATCH --output=slurm_%j.out # Standard output and error log
#SBATCH --error=slurm_%j.err # %j inserts job number
pwd; hostname; date

module load python/3.6.3
module load ncbi-blast

python half_blast.py

done