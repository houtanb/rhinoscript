import rhinoscriptsyntax as rs
from random import *

'''
# Duplicates an object N times and rotate each around a point
#
# Copyright Houtan Bastani
# 2017-2019
# License GPLv3
'''

def duplicateAndRotate():
    obj_ids = rs.GetObjects("Select object(s) to duplicate and rotate", 0, True, True)
    if obj_ids is None: return

    box = rs.BoundingBox(obj_ids)
    if not isinstance(box, list): return
    origin = rs.PointDivide(rs.PointAdd(box[0], box[6]), 2)

    endpt = rs.GetPoint("To point")
    ndups = rs.GetInteger("Number of duplications")
    maxd = rs.GetReal("Max Distance")

    translation = rs.VectorCreate(endpt, origin)
    for i in range(0, ndups, 1):
        xr = random() if random() < 0.5 else -1*random()
        yr = random() if random() < 0.5 else -1*random()
        zr = random() if random() < 0.5 else -1*random()
        newpt = [xr*maxd, yr*maxd, zr*maxd]
        translation1 = rs.VectorCreate(endpt, newpt)
        translation2 = rs.VectorCreate(translation1, origin)
        copied_obj_ids = rs.CopyObjects(obj_ids, translation2)
        xyp = rs.WorldXYPlane()
        rs.RotateObjects(copied_obj_ids, newpt, random() * 360, xyp[0])
        rs.RotateObjects(copied_obj_ids, newpt, random() * 360, xyp[1])
        rs.RotateObjects(copied_obj_ids, newpt, random() * 360, xyp[2])

if( __name__ == "__main__" ):
    duplicateAndRotate()
