def dfs(c):
    visited[c] = True
    for e in graph[c]:
        if visited[e] == False:
            visited[e] = True
            result[e] = result[c] + 1
            dfs(e)


n = int(input())    # 전체 사람의 수
a, b = map(int, input().split())    # 계산해야 할 두 사람 번호
m = int(input())    # 관계 수
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

dfs(a)
if result[b] != 0:
    print(result[b])
else:
    print(-1)