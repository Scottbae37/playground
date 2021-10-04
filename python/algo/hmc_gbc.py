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
