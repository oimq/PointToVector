from random import randint as r

class CVector2DList:
    def __init__(self, cornodelist):
        self.cornodelist = cornodelist
        self.nodelist = cornodelist.getNodes()
        self.corlist = cornodelist.getArray()
        self.veclist = list()
        self.grid = 1

    def show(self, screen, width, color):
        # show!!!!!!!!!!!!!
        for vec in self.veclist :
            screen.drawline(vec[0], vec[1], vec[2], vec[3], width, color)
        screen.update()

    def CorToVecPath(self):
        print("\n------------- start convert to vector ------------\n")

        # [ y, x ]
        # get appropriated start point
        cor = None
        dir = [0, -1]
        vecinx = 0
        for i in range(len(self.corlist)):
            cor = self.corlist[i]
            if self.cornodelist.get_surround_num(cor[0], cor[1]) > 1:
                # we select first coordi for start
                cor = list(cor)
                self.veclist.append(cor + cor)
                break
        dir = self.nextPath(self.veclist[vecinx][2:4], dir)
        print("we start coordinates :", cor)
        print("we start direction :", dir)

        count = 2*len(self.corlist)-1
        # on going algorithms
        while True :
            count -= 1
            newdir = self.nextPath(self.veclist[vecinx][2:4], dir)
            if newdir == dir:
                self.veclist[vecinx][2] += newdir[0]
                self.veclist[vecinx][3] += newdir[1]
            else:
                self.veclist.append(self.veclist[vecinx][2:4]*2)
                vecinx += 1
                self.veclist[vecinx][2] += newdir[0]
                self.veclist[vecinx][3] += newdir[1]
                dir = newdir

            # stop condition
            if count < 1 :
                break

        print("* Result     Vector Num :", len(self.veclist)) #", Vector List :", self.veclist)

        print("\n------------- end convert to vector ------------\n")

    def CorToVecMap(self):
        print("\n------------- start convert to vector map ------------\n")

        # [ y, x ]
        # get appropriated start point
        cor = None
        dir = [0, -1]
        vecinx = 0
        for i in range(len(self.corlist)):
            cor = self.corlist[i]
            if self.cornodelist.get_surround_num(cor[0], cor[1]) > 1:
                # we select first coordi for start
                cor = list(cor)
                self.veclist.append(cor + cor)
                break
        dir = self.nextPath(self.veclist[vecinx][2:4], dir)
        print("we start coordinates :", cor)
        print("we start direction :", dir)

        # on going algorithms
        while True :
            newdir = self.nextPath(self.veclist[vecinx][2:4], dir)
            if newdir == dir:
                #print("same direction.", "last dir :", dir, "new dir", newdir)
                self.veclist[vecinx][2] += newdir[0]
                self.veclist[vecinx][3] += newdir[1]
            else:
                #print("create vector.", "last dir :", dir, "new dir", newdir)
                self.veclist.append(self.veclist[vecinx][2:4]*2)
                vecinx += 1
                self.veclist[vecinx][2] += newdir[0]
                self.veclist[vecinx][3] += newdir[1]
                dir = newdir

            # stop condition
            # print("Stop Condition : veclist -", self.veclist[vecinx][2:4], ", cor -", cor)
            if self.veclist[vecinx][2:4] == cor :
                break

        print("* Result     Vector Num :", len(self.veclist)) #", Vector List :", self.veclist)

        print("\n------------- end convert to vector map ------------\n")

    def nextPath(self, cur, nextdir):
        nextdir = self.getfirstdir(nextdir[0], nextdir[1])
        for i in range(3):
            if self.cornodelist.ishave(cur[0] + nextdir[0], cur[1] + nextdir[1]) :
                return nextdir
            else:
                nextdir = self.getnextdir(nextdir[0], nextdir[1])
        #print("we don't found point to right go... so just random!")
        for i in range(r(0,3)) : nextdir = self.getnextdir(nextdir[0], nextdir[1])
        return nextdir

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

    def getArrayBias(self):
        arr = list(map(list, zip(*self.getArray())))
        barr = list()
        bias_list = list()
        for i in range(len(arr)) :
            bias_list.append((max(arr[i]), min(arr[i])))
            bvalue = abs(bias_list[i][0]) if abs(bias_list[i][0]) > abs(bias_list[i][1]) else abs(bias_list[i][1])
            barr.append(list(map(lambda n : float(n/bvalue), arr[i])))
        return list(map(list, zip(*barr)))