set terminal postscript eps color solid "Helvetica" 24
title_string = sprintf("Rebellion %s Episode %d Agent Graph", config_name, episode_num)
set title title_string
set style data lines
set output output_file
set key on bmargin horizontal
set border 3
set xtics nomirror
set ytics nomirror
set multiplot

set xrange[-0.5:1001]
set xlabel "Simulation Tick"

set yrange[0:1230]
set ylabel "Agent Count"

set datafile separator ","
plot data_filename using 1:2 title "Quiet" lt rgb "green", \
	data_filename using 1:3 title "Jailed" lt rgb "black", \
	data_filename using 1:4 title "Active" lt rgb "red"
