from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 2


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())  #m이 가로, n이 세로
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)

