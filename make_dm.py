import DataMatrix3D as dm3d
from DataMatrix3D import Segment

case = 'AAQWQ11'

dataMatrix = dm3d.DataMatrix3D(case, '14x14', [0, 0, 0], 1, Segment.cylinder, [0.8, 1.5])

dataMatrix.encode3D(case + '.stl')
