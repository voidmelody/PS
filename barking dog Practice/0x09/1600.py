from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
hx = [-2, -2, -1, -1, 2, 2, 1, 1]
hy = [-1, 1, -2, 2, -1, 1, -2, 2]
k = int(input())    # 말 이동 횟수
w, h = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))
visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == h-1 and y == w-1:
            return visited[x][y][z] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][z] == 0 and graph[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
        if z < k:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == 0:
                        if visited[nx][ny][z+1] == 0:
                            visited[nx][ny][z+1] = visited[x][y][z] + 1
                            q.append((nx, ny, z+1))
    return -1

print(bfs())
