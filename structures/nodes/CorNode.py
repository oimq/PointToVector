# y : itself being y
# xlist : having x elements
class CorNode:
    def __init__(self, _y):
        self.xlist = list()
        self.y = _y

    def __call__(self):
        return self.y

    def add(self, other):
        self.xlist.append(other)

    def remove(self, _x):
        if _x in self.xlist :
            self.xlist.remove(_x)

    def equals(self, _y, _x):
        return self.isY(_y) and self.isX(_y)

    # is there y?
    def isY(self, _y):
        return self.y == _y

    # is there x?
    def isX(self, x):
        return x in self.xlist

    def getXList(self):
        return self.xlist

    def getXNum(self):
        return len(self.xlist)