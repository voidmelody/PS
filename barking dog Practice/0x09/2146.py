from collections import deque
import sys


def divide_bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    global count
    count += 1
    graph[x][y] = count
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y]
                    q.append((nx, ny))


def bfs(x, y):
    q = deque()
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    q.append((x, y))
    n = graph[x][y]
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > 0 and graph[nx][ny] != n:
                    return dist[x][y]
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return sys.maxsize


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1. 섬들을 다른 걸로 분리 (1, 2, 3, ...)
count = 0
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and visited[i][j] == False:
            divide_bfs(i, j)

# 2. 각 섬들 좌표에서 다른 섬 만나기 최소화
result = sys.maxsize
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            result = min(result, bfs(i, j))
print(result)
