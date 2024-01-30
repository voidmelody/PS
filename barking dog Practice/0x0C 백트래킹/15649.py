N, M = map(int, input().split())
arr = []

def f():
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return

    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            f()
            arr.pop()

f()