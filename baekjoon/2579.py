n = int(input())
arr = [0 for _ in range(301)]
s = [0 for _ in range(301)]
for i in range(n):
    arr[i] = int(input())

s[0] = arr[0]
s[1] = arr[0] + arr[1]
s[2] = max(arr[0] + arr[2], arr[1] + arr[2])
for i in range(3, n):
    s[i] = max(s[i-2] + arr[i], s[i-3] + arr[i-1] + arr[i])
print(s[n-1])