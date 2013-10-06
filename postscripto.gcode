;TYPE:CUSTOM
;End GCode
M104 S0                     ;extruder heater off
M140 S0                     ;heated bed heater off (if you have it)
G91                         ;relative positioning
G1 F300 E-1
G1 X-20.0 Y-20.0 Z0.5 F9000 E-5
G28 X0 Y0                   ;move X/Y to min endstops, so the head is out of the way
M84                         ;steppers off
G90                         ;absolute positioning
