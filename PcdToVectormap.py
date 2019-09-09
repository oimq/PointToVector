import time
from dtools import draw_map
import copy
from structures.lists.CorNodeList import CorNodeList
from structures.lists.CVector2DList import CVector2DList
from structures.lists.OptiPointList import OptiPointList
from dtools.manipulate_pcd import *
from dtools.ogm import get_ogm

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
SCALE_SIZE = 8
DIMENSION = 2

def get_cor_points(coord_list) :
    opt_points = OptiPointList(coord_list, DIMENSION)
    opt_points.optimizing()
    cor_points = CorNodeList(opt_points.getArray())
    cor_points.remaining_wall()
    return cor_points

start_run_time = time.time()

'''
-- Convert from file to point array
'''
points1, bias_list1 = convert("./pcds/4floor.pcd", axisnum=DIMENSION, separator=" ")
# points2, bias_list2 = convert("./paths/pathopt2.txt", axisnum=DIMENSION, separator=",")
#raw_points = copy.deepcopy(points1)

''' 
-- convert point to vector algorithms 
-- GRID OUTER DETECTION 
'''
#
start_algo_time = time.time()
cor_points1 = get_cor_points(points1)
# cor_points2 = get_cor_points(points2)
print("Total Grid Algorithms time :", (time.time() - start_algo_time) * 1000, "ms.")

'''
-- GETTING OGM
'''
'''
print(get_ogm(cor_points))
save(get_ogm(cor_points), filename="path.txt")
'''

'''
-- GETTING vectormap
'''
# cvlist = CVector2DList(cor_points1)
# palist = CVector2DList(cor_points2)
'''
-- SAVE TO FILE
# '''
savefromarray(points1, "map-non.txt")
savefromarraywithbias(cor_points1.getArray(), "map1.txt", bias_list1, isZero=True)
# savefromarraywithbias(cor_points2.getArray(), "path1.txt", bias_list1, isZero=True)
# savefromarray(cor_points2.getArray(), "path2.txt")
'''
-- DRAWING CODES
'''
start_draw_time = time.time()

POINT_SIZE = 3
'''
screen1 = draw_map.Screen(_width= SCREEN_WIDTH, _height= SCREEN_HEIGHT,
                          _bias_list=bias_list, _scale_size=SCALE_SIZE)
'''
screen = draw_map.Screen(_width= SCREEN_WIDTH, _height= SCREEN_HEIGHT,
                         _bias_list=bias_list1, _scale_size=SCALE_SIZE)
# draw functions
# screen1.draw_non_opt_points(raw_points, POINT_SIZE)
screen.draw_opt_points(cor_points1.getNodes(), POINT_SIZE, color="black")
# screen.draw_opt_points(cor_points2.getNodes(), POINT_SIZE, color="red")

# cvlist.CorToVecMap()
# print(cvlist.getArray())
# savefromvector(cvlist.getArray(), "vecmap", [bias_list1[1]]*2)
# cvlist.show(screen, 1, "black")
#
# palist.CorToVecPath()
# print(palist.getArray())
# savefromvector(palist.getArray(), "vecpath", [bias_list1[1]]*2)
# palist.show(screen, 10, "red")

print("Total Drawing time :", (time.time() - start_draw_time) * 1000, "ms.")
print("Total Running time :", (time.time() - start_run_time) * 1000, "ms.")

screen.mainloop()
