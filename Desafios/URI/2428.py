from libs.ordenate import *

a1, a2, a3, a4 = map(int,input().split())
aaa = [a1,a2,a3,a4]

mins = ordenate_max_min(aaa)

print(mins)


if mins[0] * mins[3] == mins[1] * mins[2]:
    print("S")
else:
    print("N")