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