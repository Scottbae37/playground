# https://www.acmicpc.net/problem/1461
# 7 2
# -37 2 -6 -39 -29 11 -28

# 131

# 8 3
# -18 -9 -4 50 22 -26 40 -45

# -45 -26 -18 -9 -4 22 40 50
#  (-45 -26) 90 (-18 -9) 36 (-4 22) 52
# 158

def sol(l, m):
    if len(l) == 0:
        return 0
    offset = 0
    total = max(list(map(abs, l[offset:offset + m])))
    offset += m
    while offset + m < len(l):
        sub_list = list(map(abs, l[offset: offset + m]))
        total = total + max(sub_list) * 2
        offset += m
    if offset < len(l):
        total = total + abs(l[-1]) * 2
    return total


if __name__ == '__main__':
    n, m = map(int, input().split())
    l = list(list(map(int, input().split())))
    l.sort()

    print(sol(l, m))
