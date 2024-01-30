N, M = map(int, input().split())
arr = []

def func(start):
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return

    for i in range(start, N+1):
        if i not in arr:
            arr.append(i)
            func(i)
            arr.pop()

func(1)
