from collections import deque


def bfs():

    # 불 먼저 큐 돌리기
    while q_f:
        x, y = q_f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if graph[nx][ny] == '#' or count_f[nx][ny] >= 0:
                continue
            count_f[nx][ny] = count_f[x][y] + 1
            q_f.append((nx, ny))

    # 이후 사람 큐 돌리기
    while q_j:
        x, y = q_j.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return count_j[x][y] + 1
            if count_j[nx][ny] >= 0 or graph[nx][ny] == '#':
                continue
            if count_f[nx][ny] != -1 and count_f[nx][ny] <= count_j[x][y] + 1:
                continue
            count_j[nx][ny] = count_j[x][y] + 1
            q_j.append((nx, ny))

    return "IMPOSSIBLE"


R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 카운트 배열 정의 및 인간과 불 좌표 찾기
count_f = [[-1 for _ in range(C)] for _ in range(R)]
count_j = [[-1 for _ in range(C)] for _ in range(R)]
q_f = deque()
q_j = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            q_j.append((i, j))
            count_j[i][j] = 0
        if graph[i][j] == 'F':
            q_f.append((i, j))
            count_f[i][j] = 0
print(bfs())
