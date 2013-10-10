

wool.gcode : spinner.py postscripto.gcode preamble.gcode 
	cat preamble.gcode > wool.gcode && ./spinner.py -cx 100 -cy 100 -r1 20 -r2 24 -v 10 -s 36 -l 0.1 -e 1.0 >> wool.gcode && cat postscripto.gcode >> wool.gcode
