import numpy as np

class OptiPointList:
    def __init__(self, _list, _dimension=3, _places=0):
        self.points = _list
        self.dimension = _dimension
        self.places = _places

    def debugging(self, msg):
        print(msg+" : "+str(len(self.points)))

    def showProgress(self):
        print("")

    # rounding -> delete duplicate
    def optimizing(self):
        self.rounding()
        self.delete_dups()

    # Rounding by decimal places
    def rounding(self):
        self.debugging("Start Rounding")
        if self.dimension == 2:
            for i in range(len(self.points)):
                for j in range(self.dimension):
                    self.points[i][j] = round(self.points[i][j], self.places)
                    self.points[i][self.dimension] = 0
        self.debugging("End Rounding")

    # Delete points that have same coordinates
    def delete_dups(self):
        self.debugging("Start delete_dups")
        tups = [tuple(point) for point in self.points]
        self.debugging("We made a tuple for delete duplicates, (length : "+str(len(tups))+")")
        self.points = list(dict.fromkeys(tups))
        self.debugging("End delete_dups")

    def getArray(self):
        return self.points

    # None of decimal places points
    def getIntArray(self):
        intpoints = list()
        for point in self.points: intpoints.append([cor*(10**self.places) for cor in point])
        return intpoints