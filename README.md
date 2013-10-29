Whitney
=======
    
    $ ./spinner.py --help
    A tool for spinning fiber and making felts with 3D printers
    usage: spinner.py [-h] -cx CENTER_X -cy CENTER_Y -r1 RADIUS_1 -r2 RADIUS_2 -v
                      HEIGHT -s LAYER_STEPS -l LAYER_HEIGHT -e EXTRUDE
    
    A gcode generator for nonwoven textiles. All units are in millimeters.
    
    optional arguments:
        -h, --help       show this help message and exit
        -cx CENTER_X     X position of center
        -cy CENTER_Y     Y position of center
        -r1 RADIUS_1     bottom radius
        -r2 RADIUS_2     top radius
        -v HEIGHT        height of part
        -s LAYER_STEPS   number of steps per layer
        -l LAYER_HEIGHT  layer height
        -e EXTRUDE       cubic mm per linear mm of material
