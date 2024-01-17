from collections import deque
def bfs():
    # q 등 필요데이터 생성
    q = deque()
    # v = [[[] for _ in range(C)] for _ in range(R)] # 리스트는 O(N)
    v = [[set() for _ in range(C)] for _ in range(R)] # set는 O(1)
    ans = 1

    # q에 초기데이터(들) 삽입
    q.append((0,0,arr[0][0]))
    v[0][0].add(arr[0][0])

    while q:
        ci,cj,cv = q.popleft()
        ans = max(ans, len(cv))
        # 4방향, 범위내, 중복값이 아닌경우, 중복시퀀스 아닌경우
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in cv:
                if cv+arr[ni][nj] not in v[ni][nj]:
                    q.append((ni,nj,cv+arr[ni][nj]))
                    v[ni][nj].add((cv+arr[ni][nj]))
    return ans


R, C = map(int, input().split())
arr = list(input() for _ in range(R))

ans = bfs()
print(ans)