T = int(input())


for tc in range(1, T+1):
    li = list(map(int , input().split()))
    if (li[1] - li[0]) > 0:
        print(f'#{tc} <')
    elif (li[1] - li[0]) == 0 :
        print(f'#{tc} =')
    else:
        print(f'#{tc} >')
    

