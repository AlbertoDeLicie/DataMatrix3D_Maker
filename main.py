import DataMatrix3D as dm3d
from DataMatrix3D import Segment
from stl import mesh
import numpy as np
from ray_math import vector, centroid

point1 = np.array([1, 1, 1])
point2 = np.array([0.5, 0.5, 0.7])


case = 'AAQWQ11'


def is_inside(ray_radius, triangle, position):
    return np.sum(np.power(np.subtract(triangle[0], position), 2)) < ray_radius ** 2


def centroid(triangle):
    return np.divide(np.sum(triangle, axis=0), len(triangle))


def __is_faced(index, source_center):
    if np.inner(normals[index], vector(centroid(triangles[index]), source_center)) > 0:
        return True
    return False


if __name__ == '__main__':
    mesh_a = mesh.Mesh.from_file('sphr.stl')

    triangles = mesh_a.vectors
    normals = mesh_a.normals

    data = np.zeros(len(triangles), dtype=mesh.Mesh.dtype)

    for i in range(len(triangles)):
        in_sphere = is_inside(100, triangles[i], [0, -150, -70])
        licom = __is_faced(i, [0, -150, -70])
        if not in_sphere and licom:
            triangles[i] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    data['vectors'] = triangles

    mesh_b = mesh.Mesh(data.copy())

    mesh_b.save('test.stl')


    a = 1

