from collections import deque


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

visited_dfs = [False for _ in range(n+1)]

def bfs(c):
    q = deque()
    visited = [False for _ in range(n + 1)]
    q.append(c)
    print(c, end=" ")
    visited[c] = True
    while q:
        c = q.popleft()
        for e in graph[c]:
            if visited[e] == False:
                visited[e] = True
                q.append(e)
                print(e, end=" ")

def dfs(c):
    visited_dfs[c] = True
    print(c, end=" ")
    for c in graph[c]:
        if visited_dfs[c] == False:
            dfs(c)


dfs(v)
print()
bfs(v)



