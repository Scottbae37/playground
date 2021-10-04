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

if __name__ == '__main__':
    N = int(input())
    d = {}
    for _ in range(N):
        s = input()
        if s not in d:
            d[s] = 0
        d[s] += 1

    target = max(d.values())
    l = []
    for k, v in d.items():
        if v == target:
            l.append(k)

    print(sorted(l)[0])
