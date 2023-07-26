import json
import sys
import random
import math


voc = {}


def calc_math(start_x,start_y, x1, y1, start_p, end_p):
    if math.sqrt((start_x - x1) ** 2 + (start_y - y1) ** 2) != 0:
        voc[math.sqrt((start_x - x1) ** 2 + (start_y - y1) ** 2)] = \
            [start_p, " => ", end_p, x1, y1]
    return voc


with open('map_100.json', 'r') as file:
    information = json.load(file)
    start_point = "Reykjavik"
    cur_point = start_point
    x_start, y_start = 3409, 8338
    route = {}
    result = []
for item_1 in information['children']:
    for item in information['children']:
        voc = calc_math(x_start, y_start, item['x'], item['y'], cur_point, item['id'])
        if voc.__len__() == len(information['children'])-1:
            for j in voc.keys():
                pass
            item = j
            for i in voc.keys():
                if i < item:
                    item = i
            route[item] = voc.get(item)
            cur_point = voc.get(item)[2]
            x_start = voc.get(item)[3]
            y_start = voc.get(item)[4]

print(route)

