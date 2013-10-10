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
M83             ;set extruder to relative mode
G1 F9000        ;set feedrate
