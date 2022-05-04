import sys
sys.setrecursionlimit(10000)
t = int(input())

cab = []

# DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(a, b):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if a <= - 1 or b >= m or b <= - 1 or a >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if cab[a][b] == 1 :
        # 해당 노드 방문 처리
        cab[a][b] = 0
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(a-1, b)
        dfs(a, b-1)
        dfs(a+1, b)
        dfs(a, b+1)
        return True
    return False

while(True):
    cnt = 0

    if(t == 0): # t가 0이 되면 반복문 탈출
        break
    m, n, k = map(int, input().split())
    cab = [[0 for j in range(m)] for i in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        cab[y][x] = 1
    
    for c in range(n):
        for d in range(m):
            if dfs(c, d) == True:
                cnt += 1

    t -= 1

    print(cnt)