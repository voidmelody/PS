from collections import deque
def bfs():
    q = deque()
    q.append((startX, startY))
    while q:
        x, y = q.popleft()
        if x == targetX and y == targetY:
            return count_graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if count_graph[nx][ny] == 0:
                count_graph[nx][ny] = count_graph[x][y] + 1
                q.append((nx, ny))



dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
t = int(input())
for _ in range(t):
    n = int(input())    # 체스판 길이
    startX, startY = map(int, input().split())    # 현재 좌표
    targetX, targetY = map(int, input().split())    # 타겟 좌표
    count_graph = [[0 for _ in range(n)]for _ in range(n)]
    count_graph[startX][startY] = 1
    print(bfs())

