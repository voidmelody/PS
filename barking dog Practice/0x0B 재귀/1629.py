a, b, c = map(int, input().split())
def f(a, b, c):
    if b == 1:
        return a % c
    temp = f(a, b // 2, c)  # 2/n 제곱
    temp = temp * temp % c
    if b % 2 == 1:
        temp = temp * a % c
    return temp

print(f(a, b, c))