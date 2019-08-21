from math import cos, sin, pi

class CVector2D:
    def __init__(self, cp, mg, th):
        self.p = cp
        self.m = mg
        self.t = th

    def getcors(self):
        return [self.point[0],
                self.point[1],
                self.point[0] + (self.m * cos(self.theta * pi / 180)),
                self.point[1] + (self.m * sin(self.theta * pi / 180))]
