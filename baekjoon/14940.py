from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[-1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
