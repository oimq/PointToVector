class OptiPointList:
    def __init__(self, _list, _dimension=3, _places=0):
        self.points = _list
        self.dimension = _dimension
        self.places = _places

    # rounding -> delete duplicate
    def optimizing(self):
        self.rounding()
        self.delete_dups()

    # Rounding by decimal places
    def rounding(self):
        for i in range(len(self.points)):
            for j in range(self.dimension):
                self.points[i][j] = round(self.points[i][j], self.places)

    # Delete points that have same coordinates
    def delete_dups(self):
        self.points = list(set([tuple(point) for point in self.points]))

    def getArray(self):
        return self.points

    # None of decimal places points
    def getIntArray(self):
        intpoints = list()
        for point in self.points: intpoints.append([cor*(10**self.places) for cor in point])
        return intpoints