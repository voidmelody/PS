from collections import deque


def bfs(c):
    q = deque()
    q.append(c)
    visited[c] = True
    while q:
        t = q.popleft()
        for e in graph[t]:
            if visited[e] == False:
                q.append(e)
                visited[e] = True
                result[e] = result[t] + 1


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

bfs(a)
if result[b] != 0:
    print(result[b])
else:
    print(-1)
