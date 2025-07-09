parm 1lst_nowat.prmtop
trajin all_nowat_fixed.ncdf
strip :WAT,LIG,Na+,Cl- parmout 1lst_dry.prmtop 
trajout holo_dry_imaged.nc
run 
