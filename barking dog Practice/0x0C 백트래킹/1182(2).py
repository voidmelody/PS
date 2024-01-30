N, S = map(int, input().split())
graph = list(map(int, input().split()))


cnt = 0
arr = []

def backTrack(start):
    global cnt
    if sum(arr) == S and len(arr) > 0:
        cnt += 1

    for i in range(start, N):
        arr.append(graph[i])
        backTrack(i+1)
        arr.pop()


backTrack(0)
print(cnt)


