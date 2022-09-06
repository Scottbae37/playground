# https://www.acmicpc.net/problem/1302

# 입력 팔린 책 제목
# 출력: 최대 판매를 올린 책 제목, 동일 판매수에서는 사전순 앞선 것

# 9
# top
# top
# top
# top
# kimtop
# abc
# abc
# abc
# abc

# abc

def sol(l: list[str]):
    d = {}
    for s in l:
        if s not in d:
            d[s] = 0
        d[s] += 1
    most_frequent = max(d.values())

    ans = []
    for k, v in d.items():
        if v == most_frequent:
            ans.append(k)
    return sorted(ans)


if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        l.append(input())
    ans = sol(l)
    print(ans[0])
