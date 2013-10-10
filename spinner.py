#!/usr/bin/env python

from numpy import linspace, pi, sin, cos
from random import random
import argparse

def spin( args ) :
    center_x        = args.center_x
    center_y        = args.center_y
    radius_1        = args.radius_1
    radius_2        = args.radius_2
    height          = args.height
    layer_steps     = args.layer_steps
    layer_height    = args.layer_height
    extrude         = args.extrude

    print '\n'.join( matcone(   center_x,
                                center_y, 
                                radius_1,
                                radius_2,
                                height,
                                layer_steps,
                                layer_height,
                                extrude ) )

parser = argparse.ArgumentParser(
                description = 'A gcode generator for nonwoven textiles. All units are in millimeters.',
                prog        = 'spinner.py' )

parser.set_defaults( func=spin )

parser.add_argument('-cx',
                    action      = 'store',
                    dest        = 'center_x',
                    type        = float,
                    required    = True,
                    help        = 'X position of center' )

parser.add_argument('-cy',
                    action      = 'store',
                    dest        = 'center_y',
                    type        = float,
                    required    = True,
                    help        = 'Y position of center' )

parser.add_argument('-r1',
                    action      = 'store',
                    dest        = 'radius_1',
                    type        = float,
                    required    = True,
                    help        = 'bottom radius' )

parser.add_argument('-r2',
                    action      = 'store',
                    dest        = 'radius_2',
                    type        = float,
                    required    = True,
                    help        = 'top radius' )

parser.add_argument('-v',
                    action      = 'store',
                    dest        = 'height',
                    type        = float,
                    required    = True,
                    help        = 'height of part' )

parser.add_argument('-s',
                    action      = 'store',
                    dest        = 'layer_steps',
                    type        = int,
                    required    = True,
                    help        = 'number of steps per layer' )

parser.add_argument('-l',
                    action      = 'store',
                    dest        = 'layer_height',
                    type        = float,
                    required    = True,
                    help        = 'layer height' )

parser.add_argument('-e',
                    action      = 'store',
                    dest        = 'extrude',
                    type        = float,
                    required    = True,
                    help        = 'cubic mm per linear mm of material' )


# machine parameters for Ultimaker
MARGIN          = 20
MIN_X, MAX_X    = MARGIN, 200 - MARGIN
MIN_Y, MAX_Y    = MARGIN, 200 - MARGIN
MAX_Z           = 200

def move(   x, y, z, e, f   ) :
    #return 'G1 X%.3f Y%.3f Z%.3f E%.3f F%.3F' % ( x, y, z, e, f )
    return 'G1 X%.3f Y%.3f Z%.3f E%.3f' % ( x, y, z, e )

def cone(   center_x,
            center_y,
            radius_1,
            radius_2,
            height,
            layer_steps,
            layer_height,
            g_per_mm        ) :
    
    commands = []
        
    # geometry check; stay inside build volume
    if  center_x + radius_1 >= MAX_X or \
        center_x + radius_2 >= MAX_X or \
        center_x - radius_1 <= MIN_X or \
        center_x - radius_2 <= MIN_X or \
        center_y + radius_1 >= MAX_Y or \
        center_y + radius_2 >= MAX_Y or \
        center_y - radius_1 <= MIN_Y or \
        center_y - radius_2 <= MIN_Y or \
        height > MAX_Z :
        raise Exception( 'Machine volume trespass' )
    
    # Do two layers at Z=0 to make sure we're on the platform
    for theta in linspace( 0, 4*pi, 2*layer_steps ) :
        x = center_x + radius_1*cos( theta )
        y = center_y + radius_1*sin( theta )
        commands.append( move( x, y, 0, 1.0, 300 ) )
    
    # spiral time
    orbits = height / layer_height
    for theta in linspace( 0, orbits*2*pi, orbits*layer_steps ) :
        orbit = theta / (2*pi)
        z = orbit * layer_height
        r = radius_1 + ( radius_2 - radius_1 ) * ( z / height )
        x = center_x + r*cos( theta )
        y = center_y + r*sin( theta )
        
        commands.append( move( x, y, z, 10, 300 ) )
    
    return commands

def matcone(center_x,
            center_y,
            radius_1,
            radius_2,
            height,
            layer_steps,
            layer_height,
            g_per_mm        ) :
    
    commands = []
        
    # geometry check; stay inside build volume
    if  center_x + radius_1 >= MAX_X or \
        center_x + radius_2 >= MAX_X or \
        center_x - radius_1 <= MIN_X or \
        center_x - radius_2 <= MIN_X or \
        center_y + radius_1 >= MAX_Y or \
        center_y + radius_2 >= MAX_Y or \
        center_y - radius_1 <= MIN_Y or \
        center_y - radius_2 <= MIN_Y or \
        height > MAX_Z :
        raise Exception( 'Machine volume trespass' )
    
    # Do two layers at Z=0 to make sure we're on the platform
    for theta in linspace( 0, 4*pi, 2*layer_steps ) :
        x = center_x + radius_1*cos( theta )
        y = center_y + radius_1*sin( theta )
        commands.append( move( x, y, 0, g_per_mm, 9000 ) )
    
    # mat time
    orbits = height / layer_height
    for theta in linspace( 0, orbits*2*pi, orbits*layer_steps ) :
        orbit = theta / (2*pi)
        z = orbit * layer_height
        r = radius_1 + ( radius_2 - radius_1 ) * ( z / height )
        jump = random()
        x = center_x + r*cos( theta * layer_steps * jump )
        y = center_y + r*sin( theta * layer_steps * jump )
        
        commands.append( move( x, y, z, g_per_mm, 300 ) )
    
    return commands
   
args = parser.parse_args()
args.func(args)

