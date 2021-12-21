import sys


def get_lst(raw_path):
    path = raw_path

    f = open(path, 'r')
    lst = []
    for line in f:
        lst.append(int(line.strip("\n")))
    f.close()

    return lst


def moves_q(lst):
    ext_num = round(sum(lst)/len(lst))
    ans = []
    for i in lst:
        ans.append(abs(i-ext_num))
    return sum(ans)


raw_path = sys.argv[1]
lst = get_lst(raw_path)


print(moves_q(lst))