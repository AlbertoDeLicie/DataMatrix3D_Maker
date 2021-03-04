import numpy as np
from stl import mesh
from ray_math import vector, centroid

class Ray:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.mesh_model = None
        self.normals = None
        self.triangles = None
        self.ray_length = None
        self.ray_radius = None

    def add_mesh(self, file):
        self.mesh_model = mesh.Mesh.from_file(file)
        self._get_normals()

    def ray_cast(self, file):

    def set_pos(self, position):
        self.position = position

    def set_dir(self, direction):
        self.direction = direction

    def set_max_angle(self, ray_length, ray_radius):
        self.ray_length = ray_length
        self.ray_radius = ray_radius

    def _get_normals(self):
        self.normals = self.mesh_model.normals

    def _get_triangles(self):
        self.triangles = self.mesh_model.vectors

    def __is_inside(self, triangle):
        for i in range(3):
            return np.sum(np.power(np.subtract(triangle[i], self.position), 2)) < self.ray_radius ** 2

    def __is_faced(self, index, source_center):
        if np.inner(self.normals[index], vector(centroid(self.triangles[index]), source_center)) > 0:
            return True
        return False



