from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    width = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    width += 1
    return width

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            result.append(bfs(i, j))

if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))