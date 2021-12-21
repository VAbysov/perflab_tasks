import math
import sys


def get_args(raw_path_1, raw_path_2):
    path_1 = raw_path_1.replace('\\', '/').replace('"',"")
    path_2 = raw_path_2.replace('\\', '/').replace('"',"")

    f_1 = open(path_1, 'r')
    circle = []
    for line in f_1:
        circle.append(line.strip("\n"))
    center_coord = circle[0].split()
    center_x = float(center_coord[0])
    center_y = float(center_coord[1])
    radius = float(circle[1])
    f_1.close()

    f_2 = open(path_2, 'r')
    coord = []
    for line in f_2:
        coord.append(line.strip("\n"))
    f_2.close()

    return center_x, center_y, radius, coord


def coordinates(center_x, center_y, radius, coord):
    for c in coord:
        p_coord = c.strip("\n").split()
        p_coord_x = float(p_coord[0])
        p_coord_y = float(p_coord[1])
        if p_coord_x == center_x + radius or p_coord_x == center_x - radius:
            print("0\n")
        elif p_coord_x < center_x + radius and p_coord_x > center_x - radius:
            y = (math.sqrt(radius**2 - (p_coord_x-center_x)**2)) + center_y
            if p_coord_y == y:
                print("0\n")
            elif p_coord_y < y and p_coord_y > -y:
                print("1\n")
            else:
                print("2\n")
        else:
            print("2\n")


raw_path_1 = sys.argv[1] 
raw_path_2 = sys.argv[2]

args = get_args(raw_path_1, raw_path_2)
coordinates(args[0], args[1], args[2], args[3])
