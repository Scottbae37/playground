# ababababa
# aba

# a a a a a
# a a

# 2500, 50
# O(NM)

if __name__ == '__main__':
    s = input()
    w = input()
    cnt = 0
    i = 0
    while len(s) >= len(w) + i:
        if w == s[i:len(w) + i]:
            cnt += 1
            i += len(w)
        else:
            i += 1
    print(cnt)
