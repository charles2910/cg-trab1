import numpy as np

class Transform:
    def __init__(self):
        pass

    def translate(self, t_x, t_y):
        return np.array([
            1.0, 0.0, 0.0, t_x,
            0.0, 1.0, 0.0, t_y,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0],
        np.float32)

    def scale(self, s_x, s_y):
        return np.array([
            s_x, 0.0, 0.0, 0.0,
            0.0, s_y, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0],
        np.float32)

    def rotate(self, ang):
        return np.array([
            np.cos(ang), -np.sin(ang), 0.0, 0.0,
            np.sin(ang),  np.cos(ang), 0.0, 0.0,
            0.0,          0.0,         1.0, 0.0,
            0.0,          0.0,         0.0, 1.0],
        np.float32)

