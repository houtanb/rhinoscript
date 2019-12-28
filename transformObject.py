import rhinoscriptsyntax as rs
from random import *
import pprint
import math

'''
# Creates a matrix given an object or set of objects around a point, which serves as the lower corner
# Inputs:
#          1) Number of duplications in X direction
#          2) Random number modifying arg 1.
#               E.g. if Arg 1 is 5 and Arg 2 is 3, then possible number of objs in X ranges from 2-8,
#                    varying based on a random number draw
#          3) Same as 1) but for Y
#          4) Same as 2) but for Y
#          5) Same as 1) but for Z
#          6) Same as 2) but for Z
#
# Copyright 2019 Houtan Bastani
'''

def transformMatrix():
    obj_ids = rs.GetObjects("Select object(s) from which to create matrix", 0, True, True)
    if obj_ids is None: return

    box = rs.BoundingBox(obj_ids)
    if not isinstance(box, list): return
    origin = rs.PointDivide(rs.PointAdd(box[0], box[6]), 2)
    endpt = rs.GetPoint("To point")

    newpt = [1, 1, 1]
    translation1 = rs.VectorCreate(endpt, newpt)
    translation2 = rs.VectorCreate(translation1, origin)
    copied_obj_ids = rs.CopyObjects(obj_ids, translation2)

    for obj in copied_obj_ids:
        matrix = []
        degrees = 90.0 # Some angle
        radians = math.radians(degrees)
        c = math.cos(radians)
        s = math.sin(radians)
        matrix.append( [c,-s, 0, 0] )
        matrix.append( [s, c, 0, 0] )
        matrix.append( [0, 0, 1, 0] )
        matrix.append( [0, 0, 0, 1] )
        pprint.pprint(matrix)
        rs.ScaleObject( obj, newpt, [3, 1, -9] )
        plane = rs.ViewCPlane()
        pprint.pprint(plane)
        rs.RotateObject(obj, newpt, uniform(0, 360), plane.XAxis)
        rs.RotateObject(obj, newpt, uniform(0, 360), plane.YAxis)
        rs.RotateObject(obj, newpt, uniform(0, 360), plane.ZAxis)

if( __name__ == "__main__" ):
    transformMatrix()
