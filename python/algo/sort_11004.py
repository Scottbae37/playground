# https://www.acmicpc.net/problem/11004
# K번째 수

# 5 2
# 4 1 2 3 5

# 2

# 약 1 억연산

def merge_sort(l: list):
    # Divide
    if len(l) == 1:
        return l
    mid = int(len(l) / 2)
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    s = 0
    e = 0
    arr = list()

    # Conquer Merge
    while s < len(left) and e < len(right):
        if left[s] <= right[e]:
            arr.append(left[s])
            s += 1
        else:
            arr.append(right[e])
            e += 1
    while s < len(left):
        arr.append(left[s])
        s += 1
    while e < len(right):
        arr.append(right[e])
        e += 1
    return arr


# if __name__ == '__main__':
N, M = map(int, input().split())
l = list(map(int, input().split()))
# ans = sorted(l)
ans = merge_sort(l)
# print(ans)
print(ans[M-1])

# 일단 분할 한다.
# 사이즈가 1이 될 때까지 -> 1은 정렬이 되어있음
# 작은 것 부터 합친다.
# 남은 합친 것들은 쌓는다
for i in range(1, len(l)): # 1 2 3 4 5
    for j in range(i, len(l)): #
        if l[j-1] > l[j]:
            

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]