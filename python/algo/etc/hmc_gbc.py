# 3 3
# 50 50
# 40 40
# 10 30
# 60 76
# 18 28
# 22 50

# 36

# 3 3
# 50 90
# 10 90
# 40 50
# 50 40
# 10 100
# 40 40
#
# 10

# 2 5
# 45 10
# 55 10

# 45 70
# 50 60
# 1 20
# 1 20
# 3 65

# 60

# 6 1
# 95 5
# 1 10
# 1 10
# 1 50
# 1 10
# 1 50
# 100 60

if __name__ == '__main__':
    N, M = map(int, input().split())
    n_l = []
    m_l = []
    for _ in range(N):
        n_l.append(tuple(map(int, input().split())))
    for _ in range(M):
        m_l.append(tuple(map(int, input().split())))

    ans = 0
    n, m = 0, 0
    (n_dist, n_speed) = n_l[n]
    (m_dist, m_speed) = m_l[m]

    while True:
        if n_speed < m_speed:
            ans = max(ans, m_speed - n_speed)

        if m_dist - n_dist == 0:
            n += 1
            m += 1
            if n == len(n_l) or m == len(m_l):
                break
            (n_dist, n_speed) = n_l[n]
            (m_dist, m_speed) = m_l[m]
        elif m_dist - n_dist > 0:
            m_dist -= n_dist
            n += 1
            if n == len(n_l):
                break
            if n < len(n_l):
                (n_dist, n_speed) = n_l[n]
        else:
            n_dist -= m_dist
            m += 1
            if m == len(m_l):
                break
            if m < len(m_l):
                (m_dist, m_speed) = m_l[m]

    print(ans)


# import sys
#
# def insert_data(list_name, section):
#     for idx in range(section):
#         input_data = list(map(int, input().split()))
#         list_name.append(input_data)
#         if idx == section: break
#     return list_name
#
# def checkValidation(list):
#     totalCount = 0
#     for idx, item in enumerate(list):
#         totalCount += item[0]
#         if 100 < totalCount: return 1
#     if 100 != totalCount: return 1
#     return 0
#
# def main():
#     구간입력카운트, 운행입력카운트 = map(int, input().split())
#
#     구간정보 = list()
#     운행정보 = list()
#     최대초과량 = 0
#
#     구간정보 = insert_data(구간정보, 구간입력카운트)
#     운행정보 = insert_data(운행정보, 운행입력카운트)
#
#     if checkValidation(구간정보) != 0: sys.exit()
#     if checkValidation(운행정보) != 0: sys.exit()
#
#     운행시작위치 = 0
#
#     for idx in range(운행입력카운트):
#         운행종료위치 = 운행시작위치 + 운행정보[idx][0]
#         현재속도 = 운행정보[idx][1]
#
#         구간시작위치 = 0
#
#         for jdx in range(구간입력카운트):
#             구간종료위치 = 구간시작위치 + 구간정보[jdx][0]
#             구간제한속도 = 구간정보[jdx][1]
#
#             초과속도 = 현재속도 - 구간제한속도
#
#             if 구간종료위치 <= 운행시작위치: 0
#             elif 운행종료위치 <= 구간시작위치: 0
#             elif 0 <= 초과속도 and 최대초과량 < 초과속도:
#                 최대초과량 = 초과속도
#
#             구간시작위치 = 구간종료위치
#
#         운행시작위치 = 운행종료위치
#
#     print(최대초과량)
#
# if __name__ == "__main__":
#     main()