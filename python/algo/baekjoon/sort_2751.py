# https://www.acmicpc.net/problem/2751

# 5
# 5
# 4
# 3
# 2
# 1

# 1
# 2
# 3
# 4
# 5

# 고급정렬(퀵, 머지, 힙)이 필요한 문제
# 파이썬은 보통 1초에 2~5천만 연산

if __name__ == '__main__':
    N = int(input())
    l = list()
    for _ in range(N):
        l.append(int(input()))
    l.sort()

    for v in l:
        print(v)
