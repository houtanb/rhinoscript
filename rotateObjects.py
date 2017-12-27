import rhinoscriptsyntax as rs
from random import *

'''
# This function rotates all shapes specified by the user about
# a point specified by the user. Rotation is done in all
# three directions for each shape.
#
# Copyright Houtan Bastani
# License GPLv3
'''

def rotateObjects():
    objs = rs.GetObjects("Select objects")
    if objs is None: return

    center = rs.GetPoint("About which point?")
    if center is None: return

    for obj in objs:
        box = rs.BoundingBox(obj)
        if not isinstance(box, list): return

        xyp = rs.WorldXYPlane()
        rs.RotateObject(obj, center, random() * 360, xyp[0])
        rs.RotateObject(obj, center, random() * 360, xyp[1])
        rs.RotateObject(obj, center, random() * 360, xyp[2])

if( __name__ == "__main__" ):
    rotateObjects()
