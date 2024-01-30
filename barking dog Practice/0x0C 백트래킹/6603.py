arr = []
def backTrack(start, ar):
    if len(ar) == 6:
        print(*ar)
        return
    for i in range(start, k):
        arr.append(s[i])
        backTrack(i+1, arr)
        arr.pop()


while True:
    l = list(map(int, input().split()))
    k = l[0]
    s = l[1:]
    if k == 0:
        break
    backTrack(0, arr)
    print()



