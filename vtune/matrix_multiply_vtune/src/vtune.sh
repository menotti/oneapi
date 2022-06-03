#!/usr/bin/env bash
for an in hotspots memory-access hpc-performance gpu-offload gpu-hotspots; do 
	echo $an 
	rm -rf vtune_data && vtune -collect $an -result-dir vtune_data ./matrix.dpcpp && vtune -report summary -result-dir vtune_data -format html -report-output $an.html
done

