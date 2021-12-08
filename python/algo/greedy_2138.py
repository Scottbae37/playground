# https://www.acmicpc.net/problem/2138

# 3
# 000
# 010

# 3

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))

    # 젤 왼쪽것을 보고, 뒤집을지 말지 결정
    ans = 0
    for i in range(1, N):
        if a[i-1] != b[i-1]:
            ans += 1
            # i-1, i, i+1
            b[i-1] = ~b[i-1]
            b[i] = ~b[i]
            b[i + 1] = ~b[i + 1]
    if a != b:
        ans = -1
    print(ans)
# 000
# 010 // 만들고자 하는 전구
