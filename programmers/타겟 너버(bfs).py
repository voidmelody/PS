from collections import deque
def solution(numbers, target):
    answer = 0
    index = 0
    q = deque()
    q.append((numbers[0], index))
    q.append((-1 * numbers[0], index))
    while q:
        num, index = q.popleft()
        index += 1
        if index < len(numbers):
            q.append((num + numbers[index], index))
            q.append((num - numbers[index], index))
        else:
            if num == target:
                answer += 1
    return answer