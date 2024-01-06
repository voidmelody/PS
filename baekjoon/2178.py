from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx < 0 or ty < 0 or tx >= n or ty >= m:
                continue
            if graph[tx][ty] == 0:
                continue
            if graph[tx][ty] == 1:
                graph[tx][ty] = graph[x][y] + 1
                q.append((tx, ty))
    return graph[n-1][m-1]


n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(bfs(0,0))

