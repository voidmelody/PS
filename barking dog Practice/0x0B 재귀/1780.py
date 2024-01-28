n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = {-1: 0, 0: 0, 1: 0}


def f(row, col, n):
    start = graph[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if graph[i][j] != start:
                next = n // 3
                f(row, col, next)
                f(row, col + next, next)
                f(row, col + 2 * next, next)
                f(row + next, col, next)
                f(row + next, col + next, next)
                f(row + next, col + 2*next, next)
                f(row + 2*next, col, next)
                f(row + 2*next, col + next, next)
                f(row + 2*next, col + 2*next, next)
                return
    answer[start] += 1
    return

f(0, 0, n)

for i in answer.values():
    print(i)
