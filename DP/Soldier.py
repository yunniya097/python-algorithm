n = int(input())
s = list(map(int, input().split()))
d = [0] * 2003

cnt = 0

d[0] = 10000001

for i in range(n-1):
    if d[i] > s[i] > s[i+1]:
        d[i+1] = s[i]
    else:
        d[i+1] = d[i]
        cnt += 1

if d[n-1] > s[n-1]:
    d[n] = s[n-1]
else:
    d[n] = d[n-1]
    cnt += 1


print(cnt)