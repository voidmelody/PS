N, M = map(int, input().split())
graph = sorted(list(map(int, input().split())))

arr = []

def func(start):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(N):
        if graph[i] >= start:
            arr.append(graph[i])
            func(graph[i])
            arr.pop()



func(graph[0])