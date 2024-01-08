from collections import deque
def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 1           # 처음 방문한 것도 카운트
    graph[x][y] = 0     # 처음 방문한 것도 방문 처리
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n):
                if graph[nx][ny] == 1:
                    count += 1
                    graph[nx][ny] = 0
                    q.append((nx, ny))
    return count


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
graph = []
count_list = []
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count_list.append(bfs(i, j))

count_list.sort()
print(len(count_list))
for a in count_list:
    print(a)