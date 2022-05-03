import sys
n = int(input()) 

date = [] # 상담 진행 일수를 저장하는 리스트
money = [] # 금액을 저장하는 리스트

d = [0] * 5

for i in range(n):  # date와 money에 각각의 입력값 저장
    c, m = map(int, sys.stdin.readline().split())
    date.append(c)
    money.append(m)

for i in range(n):    
    x = date[i]+i   # 이익을 저장할 인덱스 위치 
    if(x > n+1): 
        continue
    else: # (시작한 날짜 + 진행 기간)이 N+1 보다 작거나 같아야 상담 가능
        d[x] = max(d[x], money[i] + d[i]) # d[x]와 (i번째 날짜에 일을 할 경우 받는 돈 money[i] + 이전 날짜까지 일했을 때 받는 돈 d[i])의 최대값을 d[x]에 저장한다.
        d[x+1] = max(d[x], d[x+1])
        

print(d[n])
        