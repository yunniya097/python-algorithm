N, K = map(int, input().split())
drink_arr = [int(input()) for _ in range(N)]
total_drink = sum(drink_arr)

start = 0
end = min(drink_arr) #702, mid: 351

if N == K:
    print(min(drink_arr))

else:
    while(True):
        if start > end:
            print(mid)
            break
        
        mid = (start + end) // 2

        if mid * K > total_drink:
            end = mid - 1
        else:
            count = 0
            for drink in drink_arr:
                if count >= K:
                    start = mid + 1
                count += drink // mid
            if count >= K:
                start = mid + 1
            else:
                end = mid - 1