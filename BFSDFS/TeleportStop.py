# 텔레포트 정거장
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
teleport = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)

def bfs(start):
    q = deque()
    q.append((start, 0))
    while q:
        x, d = q.popleft()
        if x == e:
            return d
        if 1 <= x <= n:
            if not visited[x]:
                visited[x] = True
                q.append((x+1, d+1))
                q.append((x-1, d+1))
                if len(teleport[x]) > 0:
                    for i in teleport[x]:
                        q.append((i, d+1))
print(bfs(s))


# import collections 
# import sys

# n, m = map(int, input().split())
# s, e = map(int, input().split())
# teleport = [[] for _ in range(n+1)]

# for _ in range(n):
#     x, y = map(int, input().split())
#     teleport[x].append(y)
#     teleport[y].append(x)


# cnt = 0
# path = s - e

# def bfs(v):
#     road = [0] * (n + 1)
#     que = collections.deque()
#     que.append(v)
#     road[v] = 1

#     while que:
#         t = que.popleft()
#         if

# def jump(road, x, y):
#     road[y] == 1

# teleport.sort()



# for j in range(teleport):
#     if s == teleport[j][0]:
#         road[teleport[j][0]] = 1
#         cnt += 1
#     elif s+1 == teleport[j][0] or s-1 == teleport[j][0]:
#         s = teleport[j][1]
#         cnt += 2

    







