#BFS를 사용해보자.
from collections import deque


m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


bfs()
flag = False
max_num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = True
        max_num = max(max_num, graph[i][j])

if flag == True:
    print(-1)
else:
    print(max_num - 1)





