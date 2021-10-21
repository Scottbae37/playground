# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=403

# 2
# 1 3 1 2
# 10 2

# 4

# A, B 라인
# N개의 작업장있음

# A1에서 최초 시작

# 1 3 1 2
# Ai 작업시간, Bi작업시간, Ai->Bi이동시간, Bi->Ai 이동시간
# 10 2
# An 작업시간, Bn작업시간

# 4: 가장 빠른 조립시간

# 1 3 1 2
# 10 2

# a1(1)  b1(3)

# a2(10)    1 ->     b2(2)
#        <- 2
#
# 선택 -> 2가지
# 1 3 1 2      10 2 1 2
# 2 11
# 최선인줄 알고 선택했더니, 다음번에 아니한만 못할 수 있다
# Greedy는 안될듯..

# Greedy 제일 오래 걸리는 애들을 제거 해 나간다

# Brust search

import sys


def sol(l, i, is_a,  total):
    global min_total
    # Basis part
    if i == len(l):
        min_total = min(min_total, total)
        return
    if total >= min_total:
        return

    # Inductive part
    (next_a, next_b, a2b, b2a) = l[i]

    if is_a:
        # 같은 라인일 경우
        sol(l, i + 1, True, total + next_a)
        # 다른 라인으로 이동 할 경우
        sol(l, i + 1, False, total + next_b + a2b)
    else:
        sol(l, i + 1, False, total + next_b)
        sol(l, i + 1, True, total + next_a + b2a)


if __name__ == '__main__':
    min_total = sys.maxsize
    n = int(input())
    l = []

    prev_a2b = 0
    prev_b2a = 0
    for _ in range(n-1):
        (a, b, a2b, b2a) = tuple(map(int, input().split()))
        l.append((a, b, prev_a2b, prev_b2a))
        prev_a2b, prev_b2a = a2b, b2a
    (a, b) = tuple(map(int, input().split()))
    l.append((a, b, prev_a2b, prev_b2a))

    sol(l, 1, True, l[0][0])

    print(min_total)

# 2
# 1 3 1 2
# 10 2

# 4

# 3
# 1 1 1 1
# 1 1 10 1
# 10 1

# 4