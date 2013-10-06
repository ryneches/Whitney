M92 E865.8880   ;steps per meter of filament
M109 S220.0     ;set heater to 220C 
G21             ;metric values
G90             ;absolute positioning
M107            ;start with the fan off
G28 X0 Y0       ;move X/Y to min endstops
G28 Z0          ;move Z to min endstops
G92 X0 Y0 Z0 E0 ;reset software position to front/left/z=0.0
G1 Z15.0 F180   ;raise to 15mm
G92 E0          ;zero the extruded length
G1 F200 E3      ;extrude 3mm
G92 E0          ;zero the extruded length again
G1 F9000        ;set feedrate

G1 X100 Y100 Z100
G1 X120 Y100 Z100 E1.0
G1 X120 Y120 Z100 E1.0
G1 X100 Y120 Z100 E1.0
G1 X100 Y100 Z100 E1.0

G2 X100 Y120 J120

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

