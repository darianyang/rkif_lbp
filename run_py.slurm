#!/bin/bash
#SBATCH --job-name=run_py_analysis
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1 
#SBATCH --cluster=smp
#SBATCH --partition=smp
#SBATCH --time=48:00:00 
#SBATCH --mail-user=dty7@pitt.edu
#SBATCH --mail-type=END,FAIL
#SBATCH --output=py_slurm.out 
#SBATCH --error=py_slurm.err 

conda activate kif

python identify_contacts.py > identify_contacts.out
