import sys
import time

CLOUD_FORMAT_LINE_NUM = 11
COORDS_NUM = 3
WALL_THRESHOLD = 0
FLOAT_MAX = sys.float_info.max
FLOAT_MIN = sys.float_info.min
SEPARATOR = " "

def convert(filename, preformat=CLOUD_FORMAT_LINE_NUM, axisnum=COORDS_NUM, separator=SEPARATOR) :
    # open file
    # filename = input("Enter the file name : ")
    # filename = './pcds/0.3M_voxel.pcd'
    fd = -1
    try :
        fd = open(filename)
    except OSError as oe :
        print(oe.__str__())
        return None

    coord_list = list()
    bias_list = [[FLOAT_MIN, FLOAT_MAX] for i in range(axisnum)]

    # read cloud format data
    if filename.split(".")[-1] == "txt":
        pass
    elif filename.split(".")[-1] == "pcd":
        for i in range(preformat): fd.readline()
    else :
        pass

    starttime = time.time()
    # get coordinates and save to list
    while True:
        line = fd.readline()
        if not line: break
        coord_list.append([float(item) for item in line.split(separator)])
        # OPTIMAL : remove floor coordinate...
        '''
        if len(coord_list[-1])>2 and coord_list[-1][2] > WALL_THRESHOLD :
            del (coord_list[-1])
            continue
        '''
        # getting bias
        for i in range(axisnum):
            if bias_list[i][0] < coord_list[-1][i]: bias_list[i][0] = coord_list[-1][i]
            if bias_list[i][1] > coord_list[-1][i]: bias_list[i][1] = coord_list[-1][i]

    fd.close()
    print("Bias information :", bias_list)
    print("Total Get Point time :", (time.time() - starttime) * 1000, "ms.")

    return coord_list, bias_list

def savefromarray(array, filename="result.txt"):
    wf = open(filename, 'w')
    for n in array: wf.write(",".join([format(s, "f") for s in n]) + "\n")
    wf.close()

def savefromvector(vectors, filename="result.txt", bias=None, centerizing=True):
    try :
        wf = open(filename, 'w')
    except OSError as oe :
        print(oe.__str__())
        return None
    mlist = [0, 0, 0, 0]
    bias = bias*2
    if centerizing :
        mlist = [(bias[1][0]+bias[1][1])/2, (bias[0][0]+bias[0][1])/2, (bias[1][0]+bias[1][1])/2, (bias[0][0]+bias[0][1])/2]
    for vec in vectors : wf.write(','.join([str((vec[i]-mlist[i])/abs(bias[i][0]-mlist[i])) for i in range(len(vec))])+'\n')
    wf.close()

def savefromarraywithbias(array, filename="result.txt", bias=None, centerizing=True) :
    if bias==None : raise(Exception("savefromarraywithbias : You didn't put bias information"))
    try :
        wf = open(filename, 'w')
    except OSError as oe :
        print(oe.__str__())
        return None
    mlist = [0, 0]
    if centerizing :
        mlist = [(bias[1][0]+bias[1][1])/2, (bias[0][0]+bias[0][1])/2]
    for elmt in array : wf.write(','.join([str((elmt[i]-mlist[i])/abs(bias[i][0]-mlist[i])) for i in range(len(elmt))])+'\n')
    wf.close()

