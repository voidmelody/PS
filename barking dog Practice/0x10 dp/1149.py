n = int(input())

d = [[0 for _ in range(3)] for _ in range(n)]
r = [0 for _ in range(n)]
g = [0 for _ in range(n)]
b = [0 for _ in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    r[i] = a[0]
    g[i] = a[1]
    b[i] = a[2]

d[0][0] = r[0]
d[0][1] = g[0]
d[0][2] = b[0]

for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + r[i]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + g[i]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + b[i]

print(min(d[n-1]))
