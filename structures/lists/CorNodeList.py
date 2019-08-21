from ..nodes.CorNode import CorNode


class CorNodeList:
    def __init__(self, _points):
        self.cnlist = list()
        self.convert_points_to_cornodes(_points)
        self.sorting()
        # for y in self.cornodelist : print(y(), y.getXList())

    # sort by y, default : ascending
    def sorting(self, _reverse=False):
        self.cnlist = sorted(self.cnlist, key=lambda c: c(), reverse=_reverse)

    # return to list [y, x]
    def getArray(self):
        return [(y(), x) for y in self.cnlist for x in y.getXList()]

    def getNodes(self):
        return self.cnlist

    # crtn -> x: 0, y: 1
    def convert_points_to_cornodes(self, points, crtn=1):
        for point in points:
            index = self.index(point[1])
            if index == -1:
                self.cnlist.append(CorNode(point[crtn]))
            self.cnlist[index].add(point[1 - crtn])

    # found: index, couldn't found: -1
    def index(self, _y):
        for cinx in range(len(self.cnlist)):
            if self.cnlist[cinx].isY(_y):
                return cinx
        else:
            return -1

    # found the index -> if none, return False immediatly, else isX results.
    def ishave(self, _y, _x):
        cinx = self.index(_y)
        if cinx < 0:
            return False
        else:
            return self.cnlist[cinx].isX(_x)

    def get_surround_num(self, _y, _x):
        count = 0
        for y in range(int(_y - 1), int(_y + 2), 1):
            for x in range(int(_x - 1), int(_x + 2), 1):
                if self.ishave(y, x) > 0:
                    count += 1
        return count - 1

    # delete points in delete-list : [(y, x) ...]
    def delete_point(self, dlist):
        for y, x in dlist:
            inx = self.index(y)
            if inx < 0: continue
            self.cnlist[inx].remove(x)
            if self.cnlist[inx].getXNum() == 0: del (self.cnlist[inx])

    ## OPTIMATIONS
    # delete vector we can never draw
    def remaining_wall(self):
        delete_list = list()
        for node in self.cnlist :
            y = node()
            for x in node.getXList() :
                num = self.get_surround_num(y, x)
                if 8 <= num or num <= 1 :delete_list.append((y, x))
        self.delete_point(delete_list)

        # while ninx < len(self.cnlist):
        #     y = self.cnlist[ninx]()
        #     xlist = self.cnlist[ninx].getXList()
        #     for x in xlist:
        #         num = self.get_surround_num(y, x)
        #         if num >= 9 or num <= 2:
        #             delete_list.append((y, x))
        #     ninx += 1
        # self.delete_point(delete_list)
