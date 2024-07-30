T = int(input())

for tc in range(1, T+1):
    list = map(int,input().split())
    S = 0
    for i in list:
        if i%2 != 0:
            S += i

    print(f'#{tc} {S}')