T = int(input())

for tc in range(1, T+1):
    list = map(int,input().split())
    a = 0
    for i in list:
        a += i
    
    print(f'#{tc} {round(a/10)}')