# * https://www.acmicpc.net/problem/2343
#   * M개의 그룹으로 나누는 문제
# <!--
#
# * N개의 강의
# * i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.
# * 단, M개의 블루레이는 모두 같은 크기이어야 한다.
# * 최소크기의 블루레이
# * 원리: 찾아야 하는 값은 블루레이의 크기
#   * 담을 수 있으면 크기를 줄이고, 담을 수 없다면 크기를 키우고
#
# 입력
# 첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다. 다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다. 각 강의의 길이는 10,000분을 넘지 않는다.
#
# 출력
# 첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.
#
#
# 예제 입력 1
# 9 3
# 1 2 3 4 5 6 7 8 9
# 예제 출력 1
# 17

# 최소값을 찾고, => 최대 크기의 레슨크기
# 최대값을 찾아서 이분 탐색 => 전체 레슨의 합

def go(size):
    global l, m

    cnt = 1
    total = 0
    for each in l:
        total += each
        if total > size:
            cnt += 1
            total = each
    return cnt <= m


if __name__ == '__main__':
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    left = max(l)
    right = sum(l)
    ans = 0
    while left <= right:
        mid = int((left + right) / 2)
        if go(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
