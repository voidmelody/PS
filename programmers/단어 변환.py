from collections import deque


def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    if target not in words:
        return 0
    while q:
        w, depth = q.popleft()
        for word in words:
            if canChange(word, w):
                if word == target:
                    return depth + 1
                q.append((word, depth+1))


def canChange(word, target):
    length = len(word)
    dif = 0
    for i in range(length):
        if word[i] != target[i]:
            dif += 1
    if dif == 1:
        return True
    else:
        return False
