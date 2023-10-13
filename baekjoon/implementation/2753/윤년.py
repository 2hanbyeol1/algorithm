import sys

year = int(sys.stdin.readline()) # 연도

if year % 4 == 0 and year % 100 != 0: # 4의 배수이면서 100의 배수가 아닐 때
    print(1)
elif year % 400 == 0: # 400의 배수일 때
    print(1)
else: print(0)