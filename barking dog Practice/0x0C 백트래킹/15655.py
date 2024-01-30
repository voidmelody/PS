N, M = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()

arr = []
def func(start):
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return

    for g in graph:
        if g not in arr and g >= start:
            arr.append(g)
            func(g)
            arr.pop()

func(graph[0])