#!/bin/bash

# Set job parameters
#SBATCH --job-name=matlab
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --partition=short-single
#SBATCH -o outmsg-%j
#SBATCH -e errmsg-%j

# Load required module
module load matlab/2022a

# Run MATLAB script
matlab -nosplash -nodesktop < slide7.m