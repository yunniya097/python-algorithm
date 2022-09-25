# 물병(1052)
n, k = map(int, input().split())
new = 1
ans = 0
f = 0

while True:
    if n < k:
        ans = -1
        break
    
    wa = n // 2
    ter = n % 2
    water = wa + ter

    if k >= water:
        if ter == 1:
            ans += new
        break
    
    else:
        if ter == 1:
            ans += new
        n = wa+ter

    f += 1
    new = 2 ** f
    
    
print(ans)