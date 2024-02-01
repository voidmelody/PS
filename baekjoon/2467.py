N = int(input())
g = list(map(int, input().split()))
start = 0
end = N-1
result = abs(g[start] + g[end])
p = (0, 0)
# 투 포인터로 쌍 짓기
while start < end:
    s = g[start] + g[end]
    if result >= abs(s):
        result = abs(s)
        p = (g[start], g[end])
    if s > 0:
        end -= 1
    else:
        start += 1

print(*p)





