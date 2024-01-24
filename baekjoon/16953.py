from collections import deque

def bfs(a):
    q = deque()
    q.append((a, 1))
    while q:
        n, t = q.popleft()
        if n > b:
            continue
        if n == b:
            return t
        q.append((n*2, t+1))
        q.append((n*10+1, t+1))
    return -1


a, b = map(int, input().split())
print(bfs(a))
