# https://www.acmicpc.net/problem/1931

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# 4

if __name__ == '__main__':
    N = int(input())
    l = [list(map(int, input().split())) for _ in range(N)]
    # 정렬
    # 먼저 끝나는 것, 끝시간이 같은 경우는 시작시간이 앞선 것
    l.sort(key=lambda v: (v[1], v[0]))

    ans = 1
    end = l[0][1]
    for (s, e) in l[1:]:
        if s >= end:
            ans += 1
            end = e
    print(ans)
