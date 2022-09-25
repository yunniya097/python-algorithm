# 리모컨(1107)
n = list(input())
m = int(input())
answer = []
mremote = 0

broken = []
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(m):
    broken.append(input().split())

remote = list(set(list) - set(broken))

if n == 0:
    print(0)
else:
    for j in n:
        if n[j] not in broken:
            answer.append(n[j])
        else:
            for k in remote:
                minus = abs(k-n[j])
                if minus == mremote:
                    

