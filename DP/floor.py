n = int(input())
sum = 0
d = [0] * 1001

for i in range(1, n+1):
    if i % 2 == 0:
        d[i] = sum + 2
    else:
        d[i] = sum + 1
    sum += d[i]

print(d[n]%796796)