from math import ceil, floor

X = 0
Y = 1
MAX = 0
MIN = 1

def get_ogm(cornodelist=None, bias_list=None):
    if cornodelist == None or bias_list == None : return None

    ogms = list()
    fills = cornodelist.getArray()
    print(ceil(bias_list[X][MIN]), floor(bias_list[X][MAX]), ceil(bias_list[Y][MIN]), floor(bias_list[Y][MAX]))
    for i in range(int(ceil(bias_list[X][MIN])), int(floor(bias_list[X][MAX])), 1):
        for j in range(int(ceil(bias_list[Y][MIN])), int(floor(bias_list[Y][MAX])), 1):
            if (i, j) in fills:
                ogms.append([i, j, 1])
            else:
                ogms.append([i, j, 0])
    return ogms
