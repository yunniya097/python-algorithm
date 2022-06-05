# 모험가 길드
n = int(input())
explorer = list(map(int, input().split()))

result = []
cnt = 0

explorer.sort() # 모험가 정렬

while True:
    m = min(explorer) # 모험가의 공포도 중 최댓값을 찾아서 m 에 저장

    if explorer[m-1] > m:
        m = explorer[m-1]
    for i in range(m): # 최소값 만큼 pop


        # if len(explorer) >= explorer[i]:
        #     # result.append(explorer.pop()) 
        #     del explorer[:i]
        #     cnt += 1

    if len(explorer) == 0:
        break

print(cnt)

