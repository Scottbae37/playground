# https://www.acmicpc.net/problem/1260

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 1 2 4 3
# 1 2 3 4

from collections import deque


def dfs(v):
    global visit, ll
    print(v, end=' ')
    visit[v] = True
    for i in ll[v]:
        if not visit[i]:
            dfs(i)


def bfs(v):
    global visit, ll
    q = deque([v])
    while q:
        v = q.pop()
        if not visit[v]:
            print(v, end=' ')
            visit[v] = True
            for each in ll[v]:
                # 연결되어있는 모든 간선 방문
                q.appendleft(each)


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    ll = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        ll[x].append(y)
        ll[y].append(x)

    visit = [False] * (N + 1)
    dfs(V)
    print()
    visit = [False] * (N + 1)
    bfs(V)
