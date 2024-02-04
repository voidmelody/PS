F = []
f = []
F.append(1)
F.append(0)
F.append(1)
F.append(1)
f.append(0)
f.append(1)
for i in range(4, 41):
    F.append(F[i-2] + F[i-1])
for i in range(2, 41):
    f.append(f[i-2] + f[i-1])

t = int(input())
for _ in range(t):
    n = int(input())
    print(F[n], f[n])

