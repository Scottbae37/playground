# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    rocks.sort()
    prev = 0
    l = []
    for each in rocks:
        gap = each - prev
        prev = each
        l.append(gap)
    l.append(distance - prev)
    l.sort()
    l = l[-n-1:]
    return l[0]


if __name__ == '__main__':
    actual = solution(25, [2, 14, 11, 21, 17], 2)
    assert actual == 4
