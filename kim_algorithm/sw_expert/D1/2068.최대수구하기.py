T = int(input())

for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    m = arr[0]    
    for i in arr :
        if i>m:
            m = i
    print(f'#{tc} {m}')