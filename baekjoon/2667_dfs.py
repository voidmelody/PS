def dfs(x, y):
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 1:
            global count
            count += 1
            graph[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
    else:
        return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
graph = []
count_list = []
count = 0
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count_list.append(count)
            count = 0
count_list.sort()
print(len(count_list))
for a in count_list:
    print(a)