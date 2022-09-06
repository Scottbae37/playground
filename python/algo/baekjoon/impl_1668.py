# https://www.acmicpc.net/problem/1668

# 트로피 높이로 인한 왼쪽에서 보이는 수 구하고, 오른쪽에서 보이는 수 구하기

# 입력: 트로피 높이(왼쪽부터)
# 출력: 왼쪽에서 보이는 수, 오른쪽에서 보이는 수

# 5
# 1
# 2
# 3
# 4
# 5

# 5
# 1

def asce_cnt(l):
    ans = 1
    start = l[0]
    for v in l[1:]:
        if start < v:
            ans += 1
        start = max(start, v)
    return ans


if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        l.append(int(input()))

    print(asce_cnt(l))
    l.reverse()
    print(asce_cnt(l))
