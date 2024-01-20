from collections import deque


def bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or nx >= h or ny >= w:
                continue
            if graph[nx][ny] == '#':
                continue
            if fire_visited[nx][ny] == -1:
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                fire_q.append((nx, ny))
    while human_q:
        x, y = human_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 경계를 벗어난 건 탈출한 거니까 정답
            if 0 > nx or 0 > ny or nx >= h or ny >= w:
                return human_visited[x][y] + 1
            if graph[nx][ny] == '#':
                continue
            if human_visited[nx][ny] != -1:
                continue
            if fire_visited[nx][ny] != -1 and fire_visited[nx][ny] <= human_visited[x][y] + 1:
                continue
            human_visited[nx][ny] = human_visited[x][y] + 1
            human_q.append((nx, ny))
    return "IMPOSSIBLE"


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
t = int(input())    # test case
for _ in range(t):
    w, h = map(int, input().split())
    fire_visited = [[-1 for _ in range(w)] for _ in range(h)]
    human_visited = [[-1 for _ in range(w)] for _ in range(h)]
    fire_q = deque()
    human_q = deque()
    graph = []
    for _ in range(h):
        graph.append(list(input()))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*' and fire_visited[i][j] == -1:
                fire_q.append((i, j))
                fire_visited[i][j] = 0
            if graph[i][j] == '@':
                human_q.append((i, j))
                human_visited[i][j] = 0
    print(bfs())

