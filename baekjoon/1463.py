from collections import deque


def bfs(x):
    count = 0
    q = deque()
    q.append((x, count))
    while q:
        x, count = q.popleft()
        if x == 1:
            return count
        if x % 3 == 0:
            q.append((x // 3, count + 1))
        if x % 2 == 0:
            q.append((x // 2, count + 1))

        q.append((x - 1, count + 1))


n = int(input())
print(bfs(n))
