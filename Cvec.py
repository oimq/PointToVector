from math import cos, sin, pi


class OptiPoints:
    def __init__(self, _list, _coordsnum):
        self.points = _list
        self.COORDS_NUM = _coordsnum

    # rounding -> delete duplicate
    def optimizing(self, _pos):
        self.round_coords_list(_pos)
        self.delete_duplicate()

    def round_coords_list(self, _pos):
        for i in range(len(self.points)):
            for j in range(self.COORDS_NUM):
                self.points[i][j] = round(self.points[i][j], _pos)

    def delete_duplicate(self):
        opt_list = list()
        for i in range(len(self.points)):
            text = ""
            for j in range(self.COORDS_NUM): text += str(self.points[i][j]) + ","
            opt_list.append(text[:-1] + "\n")
        opt_list = list(dict.fromkeys(opt_list))
        self.points = [list(map(float, item.split(','))) for item in opt_list]

    def getArray(self):
        return self.points


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


class CorNodeList:
    def __init__(self, _points):
        self.cornodelist = list()
        self.classify_points_to_cornodes(_points)
        self.sorting()
        for y in self.cornodelist :
            print(y(), y.getXList())

    # sort by y, default : ascending
    def sorting(self, _reverse=False):
        self.cornodelist = sorted(self.cornodelist, key=lambda c: c(), reverse=_reverse)

    # return to list [y, x]
    def getArray(self):
        return [(y(), x) for y in self.cornodelist for x in y.getXList()]

    def getNodes(self):
        return self.cornodelist

    # crtn -> x: 0, y: 1
    def classify_points_to_cornodes(self, points, crtn=1):
        for point in points:
            index = self.index(point[1])
            if index == -1:
                self.cornodelist.append(CorNode(point[crtn]))
            self.cornodelist[index].add(point[1 - crtn])

    # found: index, couldn't found: -1
    def index(self, _y):
        for cinx in range(len(self.cornodelist)):
            if self.cornodelist[cinx].isY(_y):
                return cinx
        else:
            return -1

    def have(self, _y, _x):
        cinx = self.index(_y)
        if cinx < 0 : return False
        else : return self.cornodelist[cinx].isX(_x)

    def get_surround_num(self, _y, _x):
        count = 0
        for y in range(int(_y - 1), int(_y + 2), 1):
            for x in range(int(_x - 1), int(_x + 2), 1):
                if self.have(y, x) > 0:
                    count += 1
        return count

    # delete point in cornodelist
    def delete_point(self, delete_list):
        for y, x in delete_list:
            inx = self.index(y)
            if inx < 0: continue
            self.cornodelist[inx].remove(x)
            if self.cornodelist[inx].getXNum() == 0:
                del (self.cornodelist[inx])

    # delete vector we can never draw
    def remaining_wall(self):
        delete_list = list()
        node_index = 0
        while node_index < len(self.cornodelist):
            y = self.cornodelist[node_index]()
            xlist = self.cornodelist[node_index].getXList()
            for x in xlist:
                num = self.get_surround_num(y, x)
                if num >= 9 or num <= 2:
                    delete_list.append((y, x))
            node_index += 1
        self.delete_point(delete_list)


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


class CVector2DList:
    def __init__(self, cornodelist):
        self.cornodelist = cornodelist
        self.nodelist = cornodelist.getNodes()
        self.corlist = cornodelist.getArray()
        self.veclist = list()
        self.grid = 1

    def CorToVec(self):
        print("\n------------- start convert to vector ------------\n")

        # [ y, x ]
        # get appropriated start point
        cor = None
        dir = [1, 0]
        vecinx = 0
        for i in range(len(self.corlist)):
            cor = self.corlist[i]
            if self.cornodelist.get_surround_num(cor[0], cor[1]) > 1:
                # we select first coordi for start
                cor = list(cor)
                self.veclist.append(cor + cor)
                break
        dir = self.nextPath(self.veclist[vecinx][2:4], dir)
        print(self.corlist)
        print("we start coordinates :", cor)
        print("we start direction :", dir)

        # on going algorithms
        while True:
            newdir = self.nextPath(self.veclist[vecinx][2:4], dir)
            if newdir == dir:
                print("same direction.", dir, newdir)
                self.veclist[vecinx][2] += newdir[0]
                self.veclist[vecinx][3] += newdir[1]
            else:
                print("create vector.", dir, newdir)
                dir = newdir
                break

        print("vectorlist result :", self.veclist)

        print("\n------------- end convert to vector ------------\n")

    def nextPath(self, cur, nextdir):
        for i in range(3):
            if self.cornodelist.findindexcornode([cur[0] + nextdir[0], cur[1] + nextdir[1]]) < 0:
                print("we can't found", [cur[0] + nextdir[0], cur[1] + nextdir[1]])
                nextdir = self.getnextdir(nextdir[0], nextdir[1])
            else:
                print([cur[0] + nextdir[0], cur[1] + nextdir[1]], "is there.")
                return nextdir
        return False

    # see right
    def getfirstdir(self, y, x):
        g = self.grid
        if y == g:
            return [0, -1]
        elif y == -g:
            return [0, 1]
        elif x == g:
            return [1, 0]
        elif x == -g:
            return [-1, 0]

    # see counterclockwise
    def getnextdir(self, y, x):
        return list(map((lambda x: x * -1), self.getfirstdir(y, x)))

    def getArray(self):
        return self.veclist
