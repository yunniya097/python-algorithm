# 특정 거리의 도시 찾기
import sys
n, m, k, x = map(int, input().split())
city = []

for i in range (n):
    a, b = int(sys.stdin.readline())
    city.append((a, b))

# DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(a, b):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if a <= - 1 or b >= m or b <= - 1 or a >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if city[a][b] == 1 :
        # 해당 노드 방문 처리
        city[a][b] = 0
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(a-1, b)
        dfs(a, b-1)
        dfs(a+1, b)
        dfs(a, b+1)
        return True
    return False

    # 아직 못품