# 숨바꼭질(1697)

n, k = map(int, input().split())
time = 0

while True:
    n0 = abs(k - (n * 2))
    n1 = abs(k - (n - 1) * 2)
    n2 = abs(k - (n + 1) * 2)

    if n == k:
        time += 1
        break
    elif n != 0 and n0 <= abs(k - n):
        minimum = min(n0, n1, n2)
        if minimum == n0:
            n = 2 * n
            time += 1
        elif minimum == n1:
            n = 2 * (n - 1)
            time += 2
        elif minimum == n2:
            n = 2 * (n + 1)
            time += 1
    else:
        if n < k:
            n = n + 1
            time += 1
        elif n > k:
            n = n - 1
            time += 1

print(time)
