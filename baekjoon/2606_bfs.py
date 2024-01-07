from collections import deque


def bfs(c):
    count = 0
    q = deque()
    q.append(c)
    visited[c] = True
    while q:
        c = q.popleft()
        for i in graph[c]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                count += 1
    return count


n = int(input())
t = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))

