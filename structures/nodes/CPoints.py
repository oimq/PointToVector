class CPoint2D:
    def __init__(self):
        self.cor = [0, 0]

    def setxy(self, x, y):
        self.cor[0] = x
        self.cor[1] = y

    def setx(self, x):
        self.cor[0] = x

    def sety(self, y):
        self.cor[1] = y