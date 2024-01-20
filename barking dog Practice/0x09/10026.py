from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return 1


def green_bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or nx >= n or ny >= n:
                continue
            if visited_green[nx][ny] == False:
                # red or green
                if graph[x][y] == 'R':
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        visited_green[nx][ny] = True
                        q.append((nx, ny))
                elif graph[x][y] == 'G':
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        visited_green[nx][ny] = True
                        q.append((nx, ny))
                # blue
                else:
                    if graph[x][y] == graph[nx][ny]:
                        visited_green[nx][ny] = True
                        q.append((nx, ny))
    return 1


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
normal_count = 0
green_count = 0
visited = [[False for _ in range(n)] for _ in range(n)]
visited_green = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            normal_count += bfs(i, j)
        if visited_green[i][j] == False:
            green_count += green_bfs(i, j)

print(normal_count)
print(green_count)
