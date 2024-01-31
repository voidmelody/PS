N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
h = 0
while start <= end:
    mid = (start + end) // 2
    result = 0
    for tree in trees:
        if tree > mid:
            result += (tree - mid)
    if result < M:
        end = mid - 1
    else:
        h = mid
        start = mid + 1
print(h)