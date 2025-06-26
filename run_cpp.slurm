#!/bin/bash
#SBATCH --job-name=run_analysis
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1 
#SBATCH --cluster=smp
#SBATCH --partition=smp
#SBATCH --time=48:00:00 
#SBATCH --mail-user=dty7@pitt.edu
#SBATCH --mail-type=END,FAIL
#SBATCH --output=cpp_slurm.out 
#SBATCH --error=cpp_slurm.err 

module purge
module load  gcc/10.2.0  openmpi/4.1.1
module load amber/24

cpptraj -i cpp.in > cpp.out
