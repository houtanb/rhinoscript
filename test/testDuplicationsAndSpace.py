import rhinoscriptsyntax as rs
import pprint
import random

'''
# Copyright 2020 Houtan Bastani
'''

def testDuplicationsAndSpace():
    print("\n testDuplicationsAndSpace commands \n")

    obj_ids = rs.GetObjects("Select object(s) from which to create the rectangular matrix", 0, True, True)
    if obj_ids is None: return

    box = rs.BoundingBox(obj_ids)
    if not isinstance(box, list): return
    origin = rs.PointDivide(rs.PointAdd(box[0], box[6]), 2)

    nXdups = rs.GetInteger("Duplications X", 1, 1)
    rXdups = rs.GetReal("Duplications X rand", 0, 0, 100) / 100

    nYdups = rs.GetInteger("Duplications Y", 1, 1)
    rYdups = rs.GetReal("Duplications Y rand", 0, 0, 100) / 100

    nZdups = rs.GetInteger("Duplications Z", 1, 1)
    rZdups = rs.GetReal("Duplications Z rand", 0, 0, 100) / 100

    nXspace = rs.GetReal("Spacing X", 1, 0)
    rXspace = rs.GetReal("Spacing X rand", 0, 0, 100)

    nYspace = rs.GetReal("Spacing Y", 1, 0)
    rYspace = rs.GetReal("Spacing Y rand", 0, 0, 100)

    nZspace = rs.GetReal("Spacing Z", 1, 0)
    rZspace = rs.GetReal("Spacing Z rand", 0, 0, 100)

    rKeep = 1 - rs.GetReal("Percent to erase", 0, 0, 100) / 100

    endpt = rs.GetPoint("To point")

    sample_near_val = lambda val, rand: random.uniform(-rand*val, rand*val)

    calc_val_int = lambda val, rand: val + int(round(random.uniform(-rand*val, rand*val)))

    xdups = calc_val_int(nXdups, rXdups)
    ydups = calc_val_int(nYdups, rYdups)
    zdups = calc_val_int(nZdups, rZdups)

    translations = []
    # Copy Points with Spacing
    for k in range(zdups):
        for j in range(ydups):
            for i in range(xdups):
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

if( __name__ == "__main__" ):
    testDuplicationsAndSpace()
