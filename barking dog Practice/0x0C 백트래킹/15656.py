N, M = map(int, input().split())
graph = sorted(list(map(int, input().split())))

arr = []

def func():
    if len(arr) == M:
        print(*arr)
        return
    for i in range(N):
        arr.append(graph[i])
        func()
        arr.pop()


func()