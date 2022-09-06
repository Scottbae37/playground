# https://www.acmicpc.net/problem/2138
# 전구와 스위치

# Input
# 3
# 000
# 010

# 출력
# 3
m = 10000000

def sol(a, b, cnt):
    if a == b:
        m = min(m, cnt)
        return
    sol(a, b, cnt)
    # 뒤집어 가는경우
    a
    sol(cnt+1)

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))


    # for i in range(1, N-1):
    #     if a[i-1] != b[i-1]:
    #         ans += 1
    #         # i-1, i, i+1
    #         b[i-1] = ~b[i-1]
    #         b[i] = ~b[i]
    #         b[i + 1] = ~b[i + 1]
    # if a != b:
    #     ans = -1
    print(ans)