import numpy as np


def vector(point2, point1, norm=True):
    if norm:
        return normalize(np.subtract(point2, point1))
    return np.subtract(point2, point1)


def normalize(n_vector):
    return np.divide(n_vector, np.sqrt(np.sum(np.power(n_vector, 2))))


def centroid(triangle):
    return np.divide(np.sum(triangle, axis=0), 3)