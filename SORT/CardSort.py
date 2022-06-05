# 카드 정렬하기
import sys

n = int(input())
cardSize = [int(sys.stdin.readline().strip()) for i in range(n)]
result = 0

if len(cardSize) == 1: #1개일 경우 비교하지 않아도 된다
    print(0)
else:
    cardSize.sort()
    while len(cardSize)>1:
        # print("cardSize:", cardSize)
        # print("len:",len(cardSize)-1)
        if(cardSize[-2] > cardSize[-1]):
            cardSize.sort()
        # print("cardSize:", cardSize)
        cardSize.append(cardSize[0] + cardSize[1])
        result+=(cardSize[0] + cardSize[1])
        del cardSize[0:2]
        # print("result:", result)

    print(result)

# 수정 필요
