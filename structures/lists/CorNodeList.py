import CorNode

class CorNodeList:
    def __init__(self, _points):
        self.cornodelist = list()
        self.classify_points_to_cornodes(_points)
        self.sorting()
        #for y in self.cornodelist : print(y(), y.getXList())

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
