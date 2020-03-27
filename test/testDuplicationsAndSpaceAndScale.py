import rhinoscriptsyntax as rs
import pprint
import random

'''
# Copyright 2020 Houtan Bastani
'''

def testDuplicationsAndSpaceAndScale():
    print("\n testDuplicationsAndSpaceAndScale commands \n")

    obj_ids = rs.GetObjects("Select object(s) from which to create the rectangular matrix", 0, True, True)
    if obj_ids is None: return

    box = rs.BoundingBox(obj_ids)
    if not isinstance(box, list): return
    origin = rs.PointDivide(rs.PointAdd(box[0], box[6]), 2)

    nXdups = rs.GetInteger("Max Duplications X", 1, 1)
    nYdups = rs.GetInteger("Max Duplications Y", 1, 1)
    nZdups = rs.GetInteger("Max Duplications Z", 1, 1)

    nXspace = rs.GetReal("Spacing X", 1, 0)
    rXspace = rs.GetReal("Spacing X rand", 0, 0, 100) / 100

    nYspace = rs.GetReal("Spacing Y", 1, 0)
    rYspace = rs.GetReal("Spacing Y rand", 0, 0, 100) / 100

    nZspace = rs.GetReal("Spacing Z", 1, 0)
    rZspace = rs.GetReal("Spacing Z rand", 0, 0, 100) / 100

    nXscale = rs.GetReal("Scale X", 1, 0)
    rXscale = rs.GetReal("Scale X rand", 0, 0, 100) / 100

    nYscale = rs.GetReal("Scale Y", 1, 0)
    rYscale = rs.GetReal("Scale Y rand", 0, 0, 100) / 100

    nZscale = rs.GetReal("Scale Z", 1, 0)
    rZscale = rs.GetReal("Scale Z rand", 0, 0, 100) / 100

    rKeep = 1 - rs.GetReal("Percent to erase", 0, 0, 100) / 100

    endpt = rs.GetPoint("To point")

    sample_near_val = lambda val, rand: random.uniform(-rand*val, rand*val)

    translations = []
    # Copy Points with Spacing
    for k in range(nZdups):
        for j in range(nYdups):
            for i in range(nXdups):
                newpt = [origin[0] + i * nXspace + sample_near_val(nXspace, rXspace),
                         origin[1] + j * nYspace + sample_near_val(nYspace, rYspace),
                         origin[2] + k * nZspace + sample_near_val(nZspace, rZspace)]
                translations = translations + [rs.VectorCreate(endpt, newpt)]

    nObjs = len(translations)
    objs_to_keep = random.sample(range(nObjs), int(round(nObjs*rKeep)))
    translations = [translations[i] for i in objs_to_keep]

    copied_objs = []
    for tr in translations:
        copied_objs = copied_objs + rs.CopyObjects(obj_ids, tr)

    for obj in copied_objs:
        bb = rs.BoundingBox(obj)
        if bb:
            centerPt = rs.PointDivide(rs.PointAdd(bb[0], bb[6]), 2)
            # pt = rs.SurfaceVolumeCentroid(obj)
            rs.ScaleObject(obj, centerPt, [nXscale + sample_near_val(nXscale, rXscale),
                                           nYscale + sample_near_val(nYscale, rYscale),
                                           nZscale + sample_near_val(nZscale, rZscale)])

if( __name__ == "__main__" ):
    testDuplicationsAndSpaceAndScale()
