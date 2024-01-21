R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    s = set()
    s.add((0, 0, graph[0][0]))
    ans = 1
    while s:
        x, y, c = s.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] not in c:
                    s.add((nx, ny, c + graph[nx][ny]))
                    ans = max(ans, len(c) + 1)
    return ans

print(bfs())
