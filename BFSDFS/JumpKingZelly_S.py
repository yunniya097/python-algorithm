# 점프왕 쪨리(small) (16173)
n = int(input())
zelly = []
visited=[[0]*n for _ in range(n)]

def zellyjump(x,y) :
    
    # 영역을 벗어났거나 이미 방문을 했다면 return
    if x <= -1 or x >= n or y <=- 1 or y >= n or visited[x][y] == 1:
        return
    
    # 방문한 곳의 이동 칸 수가 -1이라면 방문처리
    if zelly[x][y] == -1 :
        visited[x][y] = 1
        return

    visited[x][y] = 1

    # 상,하,좌,우
    zellyjump(x + zelly[x][y], y)
    zellyjump(x, y + zelly[x][y])

for i in range(n):
    z = list(map(int, input().split()))
    zelly.append(z)

zellyjump(0,0)

if visited[-1][-1] == 1 :
    print('HaruHaru')
else :
    print('Hing')
