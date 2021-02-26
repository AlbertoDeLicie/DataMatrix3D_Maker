import DataMatrix3D as dm3d
from DataMatrix3D import Segment


if __name__ == '__main__':
    datamatrix = dm3d.DataMatrix3D('ER7YH0U', '14x14', [0, 0, 0], 0.0, Segment.hemisphere, [2, 1])

    datamatrix.encode3D('ER7YH0U.stl', 7)

