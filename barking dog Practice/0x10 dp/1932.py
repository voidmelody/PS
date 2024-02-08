n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

s = [[0 for _ in range(n)] for _ in range(n)]
s[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            s[i][j] = s[i-1][0] + arr[i][j]
        elif j == i:
            s[i][j] = s[j-1][j-1] + arr[i][j]
        else:
            s[i][j] = max(s[i-1][j-1], s[i-1][j]) + arr[i][j]

print(max(s[n-1]))