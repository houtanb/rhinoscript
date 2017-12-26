import rhinoscriptsyntax as rs
from random import *

'''
# Duplicates Object specified by user
# to point specified by user
#
# Copyright Houtan Bastani
# License GPLv3
'''

def duplicateOnce():
    obj = rs.GetObject("Select objects to duplicate")
    if obj is None: return

    rs.UnselectObjects(obj)

    box = rs.BoundingBox(obj)
    if not isinstance(box, list): return
    origin = rs.PointDivide(rs.PointAdd(box[0], box[6]), 2)

    endpt = rs.GetPoint("To point")
    translation = rs.VectorCreate(endpt, origin)

    rs.CopyObject(obj, translation)

if( __name__ == "__main__" ):
    duplicateOnce()
