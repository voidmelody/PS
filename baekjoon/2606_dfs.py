n = int(input())
t = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0
for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(c):
    global count
    visited[c] = True
    count += 1
    for i in graph[c]:
        if visited[i] == False:
            dfs(i)
dfs(1)
print(count-1)


