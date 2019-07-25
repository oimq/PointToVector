import time
import draw_map
import sys
import copy
from Cvec import OptiPoints, CorNodeList, CVector2DList

start_run_time = time.time()

CLOUD_FORMAT_LINE_NUM = 11
COORDS_NUM = 3
WALL_THRESHOLD = -100
FLOAT_MAX = sys.float_info.max
FLOAT_MIN = sys.float_info.min

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 400
SCALE_SIZE = 5

coord_list = list()
bias_list = [[FLOAT_MIN, FLOAT_MAX],[FLOAT_MIN, FLOAT_MAX],[FLOAT_MIN, FLOAT_MAX]]

# open file
#filename = input("Enter the file name : ")
filename = '0.3M_voxel.pcd'
fd = open(filename)

# read cloud format data
if filename.split(".")[-1]=="pcd" :
    for i in range(CLOUD_FORMAT_LINE_NUM) : fd.readline()

start_get_time = time.time()
# get coordinates and save to list
while True :
    line = fd.readline()
    if not line : break
    coord_list.append([float(item) for item in line.split(" ")])
    # OPTIMAL : remove floor coordinate...
    if coord_list[-1][2] < WALL_THRESHOLD :
        del(coord_list[-1])
        continue
    # biasing
    for i in range(COORDS_NUM) :
        if bias_list[i][0] < coord_list[-1][i] : bias_list[i][0] = coord_list[-1][i]
        if bias_list[i][1] > coord_list[-1][i] : bias_list[i][1] = coord_list[-1][i]
print("Bias information :", bias_list)
print("Total Get Point time :", (time.time() - start_get_time) * 1000, "ms.")

raw_points = copy.deepcopy(coord_list)
fd.close()

start_algo_time = time.time()

''' 
convert point to vector algorithms 
GRID OUTER DETECTION 
'''
#
opt_points = OptiPoints(coord_list, 3)
opt_points.optimizing(0)
cor_points = CorNodeList(opt_points.getArray())
cor_points.remaining_wall()

screen = draw_map.Screen(_width= SCREEN_WIDTH, _height= SCREEN_HEIGHT,
                          _bias_list=bias_list, _scale_size=SCALE_SIZE)

cvlist = CVector2DList(cor_points)
cvlist.CorToVec(screen)

print("Total Algorithms time :", (time.time() - start_algo_time) * 1000, "ms.")

'''
DRAWING CODES
'''
'''
start_draw_time = time.time()

POINT_SIZE = bias_list[2][1]+0.5
screen1 = draw_map.Screen(_width= SCREEN_WIDTH, _height= SCREEN_HEIGHT,
                          _bias_list=bias_list, _scale_size=SCALE_SIZE)
screen2 = draw_map.Screen(_width= SCREEN_WIDTH, _height= SCREEN_HEIGHT,
                          _bias_list=bias_list, _scale_size=SCALE_SIZE)
# draw functions
screen1.draw_non_opt_points(raw_points, POINT_SIZE)
screen2.draw_opt_points(cor_points.getNodes(), POINT_SIZE)

print("Total Drawing time :", (time.time() - start_draw_time) * 1000, "ms.")
'''
print("Total Running time :", (time.time() - start_run_time) * 1000, "ms.")


screen.mainloop()