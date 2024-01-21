from collections import deque

n, m = map(int, input().split())
graph = []
count = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# [][][0] = 그냥 움직인 경우
# [][][1] = 벽 한칸 뿌시고 움직인 경우
def bfs():
    q = deque()
    q.append((0, 0, 0))
    count[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return count[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이고, 벽 파괴를 하지 않은 경우
                if graph[nx][ny] == 1 and z == 0:
                    count[nx][ny][1] = count[x][y][0] + 1
                    q.append((nx, ny, 1))
                # 벽이 아니면서, 한번도 방문하지 않은 경우
                elif graph[nx][ny] == 0 and count[nx][ny][z] == 0:
                    count[nx][ny][z] = count[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1
print(bfs())

