# https://www.acmicpc.net/problem/9251

# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
#
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
#
# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
#
# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

# ACAYKP
# CAPCAK

# 4

# 각각의 수열을 하나씩 증가하면서 테이블 갱신

if __name__ == '__main__':
    a = input()
    b = input()

    dp = [[0] * (len(a) + 1) for _ in range(len(b) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                continue
            dp[i][j] = max(dp[i][j-1], dp[i - 1][j - 1] + 1)  # 이전꺼 혹은 좌상+1한거
    print(dp[len(a)][len(b)])
