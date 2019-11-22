import rhinoscriptsyntax as rs
from random import *
import pprint


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

def getDistanceFromOrigin(origin, x, xspace, xspacerange, y, yspace, yspacerange, z, zspace, zspacerange):
    return [origin[0] + x * (xspace + uniform(-xspacerange, xspacerange)),
            origin[1] + y * (yspace + uniform(-yspacerange, yspacerange)),
            origin[2] + z * (zspace + uniform(-zspacerange, zspacerange))]

def createMatrix():
    print("\n createMatrix commands \n")

    obj_ids = rs.GetObjects("Select object(s) from which to create matrix", 0, True, True)
    if obj_ids is None: return

    box = rs.BoundingBox(obj_ids)
    if not isinstance(box, list): return
    origin = rs.PointDivide(rs.PointAdd(box[0], box[6]), 2)

    nXdups = rs.GetInteger("Duplications X", 1, 0)
    rXdups = rs.GetInteger("Duplications X range", 0, 0, nXdups)

    nYdups = rs.GetInteger("Duplications Y", 1, 0)
    rYdups = rs.GetInteger("Duplications Y range", 0, 0, nYdups)

    nZdups = rs.GetInteger("Duplications Z", 1, 0)
    rZdups = rs.GetInteger("Duplications Z range", 0, 0, nZdups)

    nXspace = rs.GetReal("Spacing X", 1, 0)
    rXspace = rs.GetReal("Spacing X range", 0, 0, nXspace)

    nYspace = rs.GetReal("Spacing Y", 1, 0)
    rYspace = rs.GetReal("Spacing Y range", 0, 0, nXspace)

    nZspace = rs.GetReal("Spacing Z", 1, 0)
    rZspace = rs.GetReal("Spacing Z range", 0, 0, nZspace)

    nXscale = rs.GetReal("Scale X", 1, 0)
    rXscale = rs.GetReal("Scale X range", 0, 0, nXscale)

    nYscale = rs.GetReal("Scale Y", 1, 0)
    rYscale = rs.GetReal("Scale Y range", 0, 0, nYscale)

    nZscale = rs.GetReal("Scale Z", 1, 0)
    rZscale = rs.GetReal("Scale Z range", 0, 0, nZscale)

    nXrotate = rs.GetReal("Rotate X", 0, 0)
    rXrotate = rs.GetReal("Rotate X range", 0, 0, nXrotate)

    nYrotate = rs.GetReal("Rotate Y", 0, 0)
    rYrotate = rs.GetReal("Rotate Y range", 0, 0, nYrotate)

    nZrotate = rs.GetReal("Rotate Z", 0, 0)
    rZrotate = rs.GetReal("Rotate Z range", 0, 0, nZrotate)

    endpt = rs.GetPoint("To point")

    nX = randint(nXdups - rXdups, nXdups + rXdups)
    nY = randint(nYdups - rYdups, nYdups + rYdups)
    nZ = randint(nZdups - rZdups, nZdups + rZdups)
    maxX = nXdups + rXdups
    maxY = nYdups + rYdups
    maxZ = nZdups + rZdups

    minX = nXdups - rXdups
    minY = nYdups - rYdups
    minZ = nZdups - rZdups

    # Create grid
    mat = [[[0 for k in xrange(maxZ)] for j in xrange(maxY)] for i in xrange(maxX)]
    nz = randint(minZ, maxZ)
    for k in range(nz):
        ny = randint(minY, maxY)
        for j in range(ny):
            thisX = randint(minX, maxX)
            for ii in range(thisX):
                mat[ii][j][k] = 1
        nx = randint(minX, maxX)
        for i in range(nx):
            thisY = randint(minY, maxY)
            for ii in range(thisY):
                mat[i][ii][k] = 1

    print("")
    pprint.pprint(mat)
    print("")

    # Copy Points with Spacing
    for k in range(maxZ):
        for j in range(maxY):
            for i in range(maxX):
                if mat[i][j][k] == 1:
                    newpt = getDistanceFromOrigin(endpt,
                                                  i, nXspace, rXspace,
                                                  j, nYspace, rYspace,
                                                  k, nZspace, rZspace)
                    translation1 = rs.VectorCreate(endpt, newpt)
                    translation2 = rs.VectorCreate(translation1, origin)
                    copied_obj_ids = rs.CopyObjects(obj_ids, translation2)
                    for obj in copied_obj_ids:
                        rs.ScaleObject(obj, newpt,
                                       [nXscale + uniform(-rXscale, rXscale),
                                        nYscale + uniform(-rYscale, rYscale),
                                        nZscale + uniform(-rZscale, rZscale)])
                        plane = rs.ViewCPlane()
                        rs.RotateObject(obj, newpt, nXrotate + uniform(-rXrotate, rXrotate), plane.XAxis)
                        rs.RotateObject(obj, newpt, nYrotate + uniform(-rYrotate, rYrotate), plane.YAxis)
                        rs.RotateObject(obj, newpt, nZrotate + uniform(-rZrotate, rZrotate), plane.ZAxis)

if( __name__ == "__main__" ):
    createMatrix()
