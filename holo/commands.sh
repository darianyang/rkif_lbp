#!/bin/bash

ambpdb -p 1lst_nowat.prmtop -c 5_eq3_nowat_fixed.rst > holo.pdb

python analyze.py all_nowat_fixed.ncdf holo_pc.dat
