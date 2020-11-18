python3 monosat.py $1 $2 >instance.sat
./minisat instance.sat instance.soln
python3 unmonosat.py $1 $2 <instance.soln
