import rhinoscriptsyntax as rs
from random import *
import pprint

'''
# Creates a matrix given an object or set of objects around a point, which serves as the lower corner
# Given a percentage, randomly creates matrix. Replications, Spacing, Rotation, Deformation all changed
#
# Copyright 2019 Houtan Bastani
'''

def createMatrix():
    print("\n createMatrix commands \n")

    obj_ids = rs.GetObjects("Select object(s) from which to create matrix", 0, True, True)
    if obj_ids is None: return

    box = rs.BoundingBox(obj_ids)
    if not isinstance(box, list): return
    origin = rs.PointDivide(rs.PointAdd(box[0], box[6]), 2)

    nXdups = rs.GetInteger("Duplications X", 1, 1)
    rXdups = rs.GetReal("Duplications X rand", 0, 0, 100) / 100

    nYdups = rs.GetInteger("Duplications Y", 1, 1)
    rYdups = rs.GetReal("Duplications Y rand", 0, 0, 100) / 100

    nZdups = rs.GetInteger("Duplications Z", 1, 1)
    rZdups = rs.GetReal("Duplications Z rand", 0, 0, 10) / 100

    nXspace = rs.GetReal("Spacing X", 1, 0)
    rXspace = rs.GetReal("Spacing X rand", 0, 0, 100)

    nYspace = rs.GetReal("Spacing Y", 1, 0)
    rYspace = rs.GetReal("Spacing Y rand", 0, 0, 100)

    nZspace = rs.GetReal("Spacing Z", 1, 0)
    rZspace = rs.GetReal("Spacing Z rand", 0, 0, 100)

    nXscale = rs.GetReal("Scale X", 1, 0)
    rXscale = rs.GetReal("Scale X rand", 0, 0, 100)

    nYscale = rs.GetReal("Scale Y", 1, 0)
    rYscale = rs.GetReal("Scale Y rand", 0, 0, 100)

    nZscale = rs.GetReal("Scale Z", 1, 0)
    rZscale = rs.GetReal("Scale Z rand", 0, 0, 100)

    nXrotate = rs.GetReal("Rotate X", 0, 0)
    rXrotate = rs.GetReal("Rotate X rand", 0, 0, 100)

    nYrotate = rs.GetReal("Rotate Y", 0, 0)
    rYrotate = rs.GetReal("Rotate Y rand", 0, 0, 100)

    nZrotate = rs.GetReal("Rotate Z", 0, 0)
    rZrotate = rs.GetReal("Rotate Z rand", 0, 0, 100)

    endpt = rs.GetPoint("To point")

    calc_val_real = lambda val, rand: val + uniform(-rand*val, rand*val)
    calc_val_int = lambda val, rand: val + int(round(uniform(-rand*val, rand*val)))

    xdups = calc_val_int(nXdups, rXdups)
    ydups = calc_val_int(nYdups, rYdups)
    zdups = calc_val_int(nZdups, rZdups)

    xspace = calc_val_real(nXspace, rXspace)
    yspace = calc_val_real(nYspace, rYspace)
    zspace = calc_val_real(nZspace, rZspace)

    xscale = calc_val_real(nXscale, rXscale)
    yscale = calc_val_real(nYscale, rYscale)
    zscale = calc_val_real(nZscale, rZscale)

    xrotate = calc_val_real(nXrotate, rXrotate)
    yrotate = calc_val_real(nYrotate, rYrotate)
    zrotate = calc_val_real(nZrotate, rZrotate)

    # Copy Points with Spacing
    for k in range(zdups):
        for j in range(ydups):
            for i in range(xdups):
                newpt = [origin[0] + i * xspace, origin[1] + j * yspace, origin[2] + k * zspace]
                translation1 = rs.VectorCreate(endpt, newpt)
#                translation2 = rs.VectorCreate(translation1, origin)
                copied_obj_ids = rs.CopyObjects(obj_ids, translation1)
                for obj in copied_obj_ids:
                    rs.ScaleObject(obj, newpt, [xscale, yscale, zscale])
                    plane = rs.ViewCPlane()
                    rs.RotateObject(obj, newpt, xrotate, plane.XAxis)
                    rs.RotateObject(obj, newpt, yrotate, plane.YAxis)
                    rs.RotateObject(obj, newpt, zrotate, plane.ZAxis)

if( __name__ == "__main__" ):
    createMatrix()
