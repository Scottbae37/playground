# https://www.acmicpc.net/problem/11399

# 5
# 3 1 4 3 2

# 32

if __name__ == '__main__':
    N = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = l[0]
    for i in range(1, len(l)):
        # 누적= 누적 + 앞구간의 시간 + 현재 걸린 시간
        ans = ans + sum(l[0:i]) + l[i]

    print(ans)
    # // 맨앞에껀 기다리는 시간 0
    #  cnt = cnt + 신규 시간