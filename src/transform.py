#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

import numpy as np

class Transform:
    '''A class used to group all the transformation matrices'''
    def __init__(self):
        pass

    def translate(self, t_x, t_y):
        '''Returns a translation matrix with offset (t_x, t_y)'''
        return np.array([
            1.0, 0.0, 0.0, t_x,
            0.0, 1.0, 0.0, t_y,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0],
        np.float32)

    def scale(self, s_x, s_y):
        '''Returns a scaling matrix with factor (s_x, s_y)'''
        return np.array([
            s_x, 0.0, 0.0, 0.0,
            0.0, s_y, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0],
        np.float32)

    def rotate(self, ang):
        '''Returns a rotation matrix with angle ang'''
        return np.array([
            np.cos(ang), -np.sin(ang), 0.0, 0.0,
            np.sin(ang),  np.cos(ang), 0.0, 0.0,
            0.0,          0.0,         1.0, 0.0,
            0.0,          0.0,         0.0, 1.0],
        np.float32)

