import sys


def circle_massive(n, m):
    massive = (list(range(1, n+1)))
    lst = []
    path = []
    f = massive[0]
    l = massive[-1]
    while l != f:
        new_interval = (list(interval for interval in massive[0:m]))
        lst.append(new_interval)
        massive = massive[m-1:] + massive[:m-1]
        l = new_interval[-1]
    for i in range(len(lst)):
        path.append(lst[i][0])
    return "".join(map(str, path))


n = int(sys.argv[1])
m = int(sys.argv[2])

print(circle_massive(n, m))
