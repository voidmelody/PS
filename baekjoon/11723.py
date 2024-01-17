import sys

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1:
        if temp[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        command = temp[0]
        num = temp[1]
        if command == "add":
            s.add(num)
        elif command == "remove":
            s.discard(num)
        elif command == "check":
            if num in s:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)
