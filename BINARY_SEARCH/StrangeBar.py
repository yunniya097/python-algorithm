# 이상한 술집
import sys

n, k = map(int, input().split())
makgeolli = [int(sys.stdin.readline().strip()) for i in range(n)]

makgeolli.sort(reverse=True)

if n == 0:
    print(0)
else:

    s = k//n
    bottle, m, cnt= (makgeolli[-1] // s), -1, 0
    print(s)
    print(bottle)
    for i in range(n-1):
        if makgeolli[i] <= (bottle * (s+1)):
            makgeolli = makgeolli[:i]
            cnt += (n-i) * s
            break

    while True:
        s = (k-cnt) // len(makgeolli)

        if bottle >= (makgeolli[m]//s):
            bottle = makgeolli[m]//s
        else:
            bottle = makgeolli[0] // (s+1)
        

        for i in range(len(makgeolli)):
            cnt += makgeolli[i] // bottle
        
        if cnt == k:
            break
        
            
    print(bottle)


# # 이상한 술집
# import sys

# n, k = map(int, input().split())
# makgeolli = [int(sys.stdin.readline().strip()) for i in range(n)]

# makgeolli.sort(reverse=True)
# s = k//n
# bottle, cnt = 0, 0

# def split(tmp, list):
#     for i in range(len(list)):
#         if (s+1) * tmp <= list[i]:
#             continue
#         else:
#             list = list[:i]
            
#             break

#     return list
    
# makgeol = makgeolli
# while True:
#     s = (k-cnt) // len(makgeol)

#     if bottle == 0:
#         bottle = makgeol[-1] // s
#     else:
#         if bottle > (makgeol[-1] // s):
#             bottle = makgeol[0] // (s+1)

#         else:
#             bottle = makgeol[-1] // s

#     mak = split(bottle, makgeol)
#     cnt += (len(makgeol)-len(mak)) * s

#     if not mak:
#         break
#     else:
#         makgeol = mak
        


# print(cnt)



# print(makgeolli)

# bottle, m= 0, n-1





# makgeol = makgeolli[:n//2]

# while True:
    
#     # print(m,s)
#     bottle = makgeolli[m]//s
#     print("bot", bottle)
    
#     for i in range(n):
#         if (s+1) * bottle <= makgeolli[i]:
#             cnt += makgeolli[i] // bottle
#         else:
#             makgeolli = makgeolli[:i]
#             cnt += (n-i) * s
#             break
    
#         # print('cnt:', cnt)
    
#     if cnt == k:
#         break
#     else:
#         cnt = (n-len(makgeolli)) * s
#         if bottle < makgeolli[-1]:
#             m = 0
#             s += 1
#         else:
#             if len(makgeolli) > 1:
#                 m = len(makgeolli) - 1
#                 s = k//n
        
        
        
# print(bottle)

