# https://www.acmicpc.net/problem/1568

# N마리 새
# 1부터 증가하며, 증가하는 수 만큼 새가 날라가
# 남아있는새가 증가값보다 작다면 1부터 다시 시작

# 입력: 새 수
# 출력: 몇 번째 노래

# 14
# 7

if __name__ == '__main__':
    N = int(input())
    i = 1
    ans = 1
    N -= i
    while N != 0:
        i += 1
        if i > N:
            i = 1
        N -= i
        ans += 1
    print(ans)
