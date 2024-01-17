from collections import deque

visited = [0 for _ in range(200000)]
n, k = map(int, input().split())

q = deque()
q.append(n)
visited[n] = 1
while q:
    x = q.popleft()
    if x == k:
        print(visited[x] - 1)
        break
    for a in (x-1, x+1, x*2):
        if 0 <= a <= 100000 and visited[a] == 0:
            q.append(a)
            visited[a] = visited[x] + 1
