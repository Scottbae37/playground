# https://www.acmicpc.net/problem/2212

# 6
# 2
# 1 6 9 3 6 7

# 5

# 안테나 K(2)개 설치

# 정렬을 수행한다
# 각 구간의 길이차를 구한다
# 가장 길이가 긴 구간부터 제거한다 until K-1까지
# 각 구간 간격을 모두 합하면 안테나 포함 범위 최소 걸이
import sys

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = list(map(int, input().split(' ')))
    if k >= n:
        print(0)
        sys.exit()
    arr.sort()

    l = []
    for i in range(n - 1):
        l.append(arr[i + 1] - arr[i])

    l.sort(reverse=True)
    for i in range(k - 1):
        l[i] = 0
    print(sum(l))
