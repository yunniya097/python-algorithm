n = int(input()) # n 입력 받기
confer = [] # 입력 받은 회의 시간을 저장할 리스트
result = [] # 결과 리스트

# 회의 정보를 confer에 튜플 형태로 저장
for i in range(n):
    c = tuple(map(int, input().split()))
    confer.append(c)

confer.sort()

i = 0
n = 1

print(confer)
print(result)