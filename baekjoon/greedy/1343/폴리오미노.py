str = input()

count = 0
ans = ''

for s in str:
    if s == 'X':
        count += 1
        if count == 4:
            ans += 'AAAA'
            count = 0
    else:
        if count == 2:
            ans += 'BB'
            count = 0
        elif count % 2 != 0:
            ans = -1
            break
        ans += '.'

if count == 4:
    ans += 'AAAA'
elif count == 2:
    ans += 'BB'
elif count % 2 != 0:
    ans = -1

print(ans)