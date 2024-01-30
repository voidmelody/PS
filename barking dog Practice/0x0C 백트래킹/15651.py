N, M = map(int, input().split())
arr = []

def func():
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return

    for i in range(1, N+1):
        arr.append(i)
        func()
        arr.pop()

func()