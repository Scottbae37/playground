# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=392

# 4
# 1 3
# 2 4
# 3 5
# 3 3

# 3

# 3
# 1 3
# 2 4
# 3 5

# 2

if __name__ == '__main__':
    N = int(input())
    input_list = []
    for _ in range(N):
        input_list.append(tuple(map(int, input().split())))
    l = sorted(input_list, key=lambda v: (v[1], v[0]))
    i = 0
    (s, e) = l[i]
    ans = 1
    for (n_s, n_e) in l[1:]:
        if n_s < e:
            continue
        ans += 1
        e = n_e
    print(ans)
