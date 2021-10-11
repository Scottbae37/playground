# https://www.acmicpc.net/problem/1012

# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

# 5
# 1
from collections import deque

def in_range(x, y):
    global X, Y
    if X <= x:
        return False
    if Y <= y:
        return False
    if x < 0:
        return False
    if y < 0:
        return False
    return True


dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, ll):
    q = deque()
    q.append((x, y))
    while q:
        (tmp_x, tmp_y) = q.pop()
        for (x, y) in dir:
            nx = tmp_x - x
            ny = tmp_y - y
            if in_range(nx, ny) and ll[ny][nx] == 1:
                ll[ny][nx] = 0
                q.append((nx, ny))


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        X, Y, N = map(int, input().split())
        ll = [[0] * X for _ in range(Y)]
        for _ in range(N):
            nx, ny = map(int, input().split())
            ll[ny][nx] = 1

        visit = [[False] * X for _ in range(Y)]
        cnt = 0
        for y in range(Y):
            for x in range(X):
                if ll[y][x] == 1:
                    cnt += 1
                    ll[y][x] = 0
                    bfs(x, y, ll)
        print(cnt)