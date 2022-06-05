# 주몽
import sys
n = int(input())
m = int(input())
armor = list(map(int, sys.stdin.readline().split()))

armor.sort()
s, cnt = 0, 0
e = n-1

if armor[e-1] + armor[e] < m:
    print(cnt)
else:
    while s < e:
        if armor[s] + armor[e] == m:
            cnt += 1
            s += 1
            e -= 1
        elif armor[s] + armor[e] < m:
            s += 1
        else:
            e -= 1

    print(cnt)

