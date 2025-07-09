#!/bin/bash

# first needed a pdb file to check where the Cu atoms were
ambpdb -p 1lst_nowat.prmtop -c 5_eq3_nowat_fixed.rst > holo.pdb

# then analyzed it using updated script
python analyze.py all_nowat_fixed.ncdf holo_pc.dat

# later on ended up making a version of the ncdf traj without the ligand at all for full consistency with the other traj data
cpptraj -i strip.cpp > strip.out
