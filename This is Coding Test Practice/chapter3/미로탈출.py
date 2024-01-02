"""
첫째 줄에 두 정수 N, M이 주어집니다.
다음 N개의 줄에는 각각의 M개의 정수 (0 or 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
또한 시작 칸과 마지막 칸은 1이다.
"""

# 최소 거리를 구해야 하므로, BFS
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]


print(bfs(0, 0))

