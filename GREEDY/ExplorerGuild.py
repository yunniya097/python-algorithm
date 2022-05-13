# 모험가 길드
n = int(input())
explorer = list(map(int, input().split()))

result = []
cnt = 0

explorer.sort() # 모험가 정렬

while True:
    m = max(explorer) # 모험가의 공포도 중 최댓값을 찾아서 m 에 저장
    for i in range(m): # 최댓값 만큼 pop
        result.append(explorer.pop()) 
    cnt += 1

    if len(explorer) == 0:
        break

print(cnt)