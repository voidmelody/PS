N, S = map(int, input().split())
graph = list(map(int, input().split()))


cnt = 0
def backTrack(index, total):
    if index == N:
        if total == S:
            global cnt
            cnt += 1
        return
    backTrack(index+1, total)
    backTrack(index+1, total + graph[index])


backTrack(0, 0)
if S == 0:
    cnt -= 1
print(cnt)


