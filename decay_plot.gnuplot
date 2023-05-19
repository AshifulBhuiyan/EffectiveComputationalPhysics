#decay_plot.gnuplot
set title 'Decays'
set ylabel 'Decays '
set xlabel 'Time (s)'
set grid
set term svg
set output 'plot_gnuplots.svg'
plot '~/Python/effectivephysics-textbook/examples/data/decays.csv' every ::1 using 1:2 with lines
