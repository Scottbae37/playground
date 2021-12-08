import itertools

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(1, n + 1):
        l.append(i)
    permutations = itertools.permutations(l, n)
    ans = sorted(list(permutations))
    for v in ans:
        print(v)
