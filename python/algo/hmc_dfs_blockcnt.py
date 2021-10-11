# 7
# 1110111
# 0110101
# 0110101
# 0000100
# 0110000
# 0111110
# 0110000

# 블록수, 블록내 장애물 수(오름차순)
# 3
# 7
# 8
# 9

def in_range(x, y):
    global N
    if x >= N:
        return False
    if y >= N:
        return False
    if x < 0:
        return False
    if y < 0:
        return False
    return True


def dfs(x, y, l):
    cnt = 1
    for (nx, ny) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx += x
        ny += y
        if not in_range(nx, ny):
            continue
        if l[nx][ny] == 1:
            l[nx][ny] = 0
            cnt += dfs(nx, ny, l)
    return cnt


if __name__ == '__main__':
    N = int(input())
    l = [list(map(int, input())) for _ in range(N)]

    ans = 0
    ansList = []
    for i in range(N):
        for j in range(N):
            if l[i][j] == 1:
                l[i][j] = 0
                ans += 1
                ansList.append(dfs(i, j, l))
    ansList.sort()
    print(ans)
    for v in ansList:
        print(v)
