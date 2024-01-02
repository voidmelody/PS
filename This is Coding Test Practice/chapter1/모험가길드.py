n = map(int, input())
members = list(map(int, input().split()))
members.sort()
result = 0
members_set = set(members)
for i in members_set:
    if members.count(i) >= i:
        result += 1
print(result)
