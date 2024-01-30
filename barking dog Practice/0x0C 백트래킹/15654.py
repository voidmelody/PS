N, M = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()
arr = []

def func():
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return

    for g in graph:
        if g not in arr:
            arr.append(g)
            func()
            arr.pop()

func()