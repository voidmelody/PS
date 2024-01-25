from collections import deque


def bfs(z, x, y):
    q = deque()
    q.append((z, x, y))
    visited[z][x][y] = True
    dist[z][x][y] = 0
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                if graph[nz][nx][ny] == 'E':
                    return dist[z][x][y] + 1
                if graph[nz][nx][ny] == '.' and visited[nz][nx][ny] == False:
                    visited[nz][nx][ny] = True
                    dist[nz][nx][ny] = dist[z][x][y] + 1
                    q.append((nz, nx, ny))
    return 0


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]    # 북 동 남 서 상 하

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    graph = []
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    dist = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for _ in range(L):
        t = []
        for _ in range(R):
            t.append(list(input()))
        graph.append(t)
        input()     # \n 제거
    for i in range(L):
        for j in range(R):
            for t in range(C):
                if graph[i][j][t] == 'S':
                    result = bfs(i, j, t)
    if result == 0:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(result))