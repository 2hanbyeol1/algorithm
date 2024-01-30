import sys

N = int(sys.stdin.readline())
sk = list(map(int, sys.stdin.readline().split())) # 상근이 숫자 카드
sk.sort()

M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

# 배열 안에 e가 포함되어 있는지 탐색
def search(e, sortedArr):
    start = 0
    end = len(sortedArr) - 1
    while start <= end:
        mid = (start + end) // 2
        if sortedArr[mid] == e:
            return True
        elif sortedArr[mid] < e: start = mid + 1
        else: end = mid - 1
    return False

# cards의 카드 각각이 상근이가 가진 카드인지 구별
for card in cards:
    if search(card, sk):
        print(1, end=' ')
    else: print(0, end=' ')