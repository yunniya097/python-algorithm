# 숫자 정사각형

n, m = map(int, input().split())
rec = []
result = []

for i in range(n):
    rec.append(list(input()))
    
# 길이가 1이면 그냥 1
if n == 1 or m == 1:
    print(1)

else:
    for i in range(n):
        for j in range(m):
            dot = rec[i][j]
            if j == m: # j가 m이랑 같으면 길이가 초과됨
                break
            else:
                x = j+1
                while True:
                    if x > m-1: # x가 행의 길이보다 길면 break
                        break
                    else:
                        #print(i, j, x)
                        if dot == rec[i][x]:
                            if x-j > n-1:
                                break
                            else:
                                if rec[x-j][j] == dot and rec[x-j][x] == dot:
                                    result.append(((x-j+1)**2))
                                    #print('check: ', i, j, x)
                                    #print(rec[i][j], rec[i][x-j], rec[x-j][j], rec[x-j][x])
                                x += 1
                        else:
                            x += 1
    if not result:
        print(1)
    else:
        print(max(result))


            

# else:
#     for i in range(n):
#         for j in range(m):
#             try:
#                 cnt[rec[i][j]] += 1
#             except:
#                 cnt[rec[i][j]] = cnt[rec[i][j]]
    
#     if 4 not in cnt:
#         print(1)

#     else:
#         c = cnt.count(4)
#         if c == 1:
#             idx = list(filter(lambda e:rec[e] == cnt.index(4), range(m)))
#             print(idx)


# for i in range(n):
#     rec[i] = list(map(int, sys.stdin.readline().rstrip()))
#     for j in range(m):
#         try:
#             cnt[i][rec[i][j]] += 1
#         except:
#             cnt[i][rec[i][j]] = cnt[i][rec[i][j]]

# a = 0
# b = a + 1
# while True:
#     if a > n:
#         break
    
#     if 2 in cnt[a]:
#         if 2 in cnt[b]:
#             if cnt[a].index == cnt[b].index:
#                 tmpA = list(filter(lambda e:rec[e] == cnt[a].index, range(m)))
#                 tmpB = list(filter(lambda e:rec[e] == cnt[b].index, range(m)))

#                 if tmpA[0] == tmpB[0] and tmpA[1] == tmpB[1]:
                    
#             else:
#         else:
#             b += 1
#     else:
#         a += 1
#         b = a + 1

