import rhinoscriptsyntax as rs
from random import *

'''
# This function rotates all shapes specified by the user about
# a point specified by the user. Rotation is done in all
# three directions for each shape.
#
# Copyright Houtan Bastani
# 2017-2019
# License GPLv3
'''

def rotateObjects():
    obj_ids = rs.GetObjects("Select objects", 0, True, True)
    if obj_ids is None: return

    center = rs.GetPoint("About which point?")
    if center is None: return

    xyp = rs.WorldXYPlane()
    rs.RotateObjects(obj_ids, center, random() * 360, xyp[0])
    rs.RotateObjects(obj_ids, center, random() * 360, xyp[1])
    rs.RotateObjects(obj_ids, center, random() * 360, xyp[2])

if( __name__ == "__main__" ):
    rotateObjects()
