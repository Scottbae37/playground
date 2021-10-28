# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

# 6 [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# 3

import queue


# BFS max 깊이 구하기
# 깊이별 연결 노드들 저장
# max 깊이와 같은 노드의 수를 리턴

def solution(n, edge):
    matrix = [[] for _ in range(n + 1)]
    for e in edge:
        a, b = e[0], e[1]
        matrix[a].append(b)
        matrix[b].append(a)
    ans = {}

    max_depth = 0
    for i in range(2, n + 1):
        visit = [0] * 20001
        visit[i] = n + 1
        q = queue.LifoQueue()
        q.put((i, 0))
        min_depth = n
        while not q.empty():
            (v, depth) = q.get()
            if v == 1:
                min_depth = min(min_depth, depth)
                continue
            for each in matrix[v]:
                if visit[each] == 0 or visit[each] > depth + 1:
                    visit[each] = depth + 1
                    q.put((each, depth + 1))
        if min_depth not in ans:
            ans[min_depth] = []
        ans[min_depth].append(i)
        max_depth = max(max_depth, min_depth)
    return len(ans[max_depth])


# if __name__ == '__main__':
#     actual = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [6, 4]])
#     print(actual)
#     assert actual == 3


import queue


# def solution(n, edge):
#     matrix = [[] for _ in range(n + 1)]
#     for e in edge:
#         a, b = e[0], e[1]
#         matrix[a].append(b)
#         matrix[b].append(a)
#     visit = [False] * 20001
#     visit[1] = True
#     ans = {}
#
#     max_depth = 0
#     q = queue.LifoQueue()
#     q.put((1, max_depth))
#     while not q.empty():
#         (v, depth) = q.get()
#         for each in matrix[v]:
#             if not visit[each]:
#                 visit[each] = True
#                 q.put((each, depth + 1))
#                 if (depth + 1) not in ans:
#                     ans[depth + 1] = []
#                 ans[depth + 1].append(each)
#                 max_depth = max(max_depth, depth + 1)
#     return len(ans[max_depth])

if __name__ == '__main__':
    actual = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [6, 4]])
    print(actual)
    assert actual == 3