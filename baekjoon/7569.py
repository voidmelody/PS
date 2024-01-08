from collections import deque
def bfs():
    q = deque()
    for z in range(h):
        for i in range(n):
            for j in range(m):
                if graph[z][i][j] == 1:
                    q.append((z, i, j))

    while q:
        z, x, y = q.popleft()
        for i in range(len(dx)):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
bfs()

max_num = 0
flag = False
# max 구하기
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                flag = True # 다 익지 못함.
            max_num = max(max_num, graph[z][x][y])

if flag == True:
    print(-1)
else:
    print(max_num - 1)



