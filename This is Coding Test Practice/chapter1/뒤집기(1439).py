str = list(map(int, input()))
target = str[0]
zero_count = 0
first_count = 0

if target == 0:
    zero_count += 1
else:
    first_count += 1

for s in str:
    if s != target:
        if s == 0:
            zero_count += 1
        else:
            first_count += 1
        target = s

print(min(zero_count, first_count))

