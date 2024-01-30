n = int(input()) # 거스름돈 액수
coin_2, coin_5 = 0, 0

while n > 0:
    if n % 5 == 0:
        coin_5 = n // 5
        n = 0
    else:
        coin_2 += 1
        n -= 2

if n == 0:
    print(coin_2 + coin_5) # 거스름돈 동전의 최소 개수
else: print(-1) # 거슬러 줄 수 없으면 -1