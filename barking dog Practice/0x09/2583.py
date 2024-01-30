from collections import deque


# x, y 반대다 조심해라
M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
width = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(K):
    ly, lx, ry, rx = map(int, input().split()) # 왼쪽 아래, 오른쪽 위-> -1
    for i in range(lx, rx):
        for j in range(ly, ry):
            graph[i][j] = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                count += 1
                q.append((nx, ny))
    return count


for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and visited[i][j] == False:
            width.append(bfs(i, j))

width.sort()
print(len(width))
for w in width:
    print(w, end=" ")




