# n = int(input())
# k = int(input())

# a = 0
# b = k//n

# while True:
#     if a <= b < a+1:
#         i = a+1
#         break
#     else:
#         a += 1 

# j = k%n + 1

# ans = i * j

# if ans < (n**2):
#     print(ans)

###############

# n = int(input())
# k = int(input())

# B = []
# s = 0

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         a = i*j
#         B.append(a)
# B.sort

# print(B[k])
#####################
# n = int(input())
# k = int(input())

# a = n * 2 - 1

# if k == 0:
#     ans = 1
# elif 0 < k <= a:
#     if k%2 == 1:
#         ans = k // 2 + 2
#     elif k%2 == 0:
#         ans = k // 2 + 1
# elif a < k:
    