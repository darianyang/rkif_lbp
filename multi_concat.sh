#!/bin/bash
# concat all traj files into one

# Extract the third column and remove ".ncrst" extension
names=$(awk '{print $3}' ../bstates.txt | sed 's/\.ncrst$//')

# start the 
CMD="     parm ../1lst.prmtop \n"

# Loop through the names
for name in $names; do
    echo "$name"
    #cd ../$name

   #CMD="$CMD trajin ../${name}/md01.nc 1 last 10\n"
   CMD="$CMD trajin ../${name}/md02.nc 1 last 10\n"
   CMD="$CMD trajin ../${name}/md03.nc 1 last 10\n"

    #python ../analyze.py md03.nc pc_600ns.dat &&
    #echo "DONE with: ${name}"

    #cd ..
done

# finish the cpp script
CMD="$CMD autoimage \n"
CMD="$CMD strip :WAT,Na+,Cl- parmout 1lst_dry.prmtop \n"
CMD="$CMD trajout 200-600ns_dry_imaged_10i.nc \n"
CMD="$CMD run \n"

echo -e $CMD > cpp.in
#cpptraj -i cpp.in
