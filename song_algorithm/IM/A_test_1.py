import sys
sys.stdin=open('input.txt')

def start(j):
    black = 1 # 블럭수
    black_power=1
    cnt=0 #하강 칸 수
    i=1
    while i<N:
        if arr[i][j]==0:    # 블록이 없으면
            cnt+=1
            black_power*=1.9
            i+=1
            continue

        # 블록을 만났을 때는
        # 하강 블록이 이길경우 와 진 경우 두개로
        if arr[i][j]==1:
            # 만난 불록의 무게 계산
            bl_2=1
            for i_2 in range(i+1,N): #i에서 N까지 반복
                if arr[i_2][j]==1: #블록 갯수만큼 세기
                    bl_2+=1
                else:
                    break
            if black_power > bl_2: #무게저항을 이기면
                cnt=0
                black +=bl_2
                black_power+=bl_2
                i+=bl_2
                continue
            else:
                for k in range(i): # 그전까지 변화업데이트
                    if cnt:
                        arr[k][j]=0
                        cnt-=1
                    else:
                        arr[k][j]=1
                return
    for x in range(N):
        if cnt:
            arr[x][j] = 0
            cnt-=1
        else:
            arr[x][j] = 1
    return

def start2(i):
    black = 1 # 블럭수
    cnt=0 #하강 칸 수
    j=1
    black_power = 1
    while j<N:
        if arr[i][j]==0:    # 블록이 없으면
            black_power *= 1.9
            cnt+=1
            j+=1
            continue

        # 블록을 만났을 때는
        # 하강 블록이 이길경우 와 진 경우 두개로
        if arr[i][j]==1:
            # 만난 불록의 무게 계산
            bl_2=1
            for j_2 in range(j+1,N): #i에서 N까지 반복
                if arr[i][j_2]==1: #블록 갯수만큼 세기
                    bl_2+=1
                else:
                    break

            if black_power > bl_2:  # 무게저항을 이기면
                cnt=0
                black_power += bl_2
                black +=bl_2
                j+=bl_2
                continue
            else:
                for k in range(j): # 그전까지 변화업데이트
                    if cnt:
                        arr[i][k]=0
                        cnt-=1
                    else:
                        arr[i][k]=1
                return
    for x in range(N):
        if cnt:
            arr[i][x] = 0
            cnt-=1
        else:
            arr[i][x] = 1
    return


for tc in range(1,2):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    for j in range(N):
        if arr[0][j]==1:
            start(j)
    for i in range(N):
        if arr[i][0]==1:
            start2(i)
    cnt_row=0
    cnt_col=0
    for z in range(N):
        if arr[z][N-1]==1: # 맨오른쪽 열
            cnt_col+=1
        if arr[N-1][z]==1:
            cnt_row+=1

    print(f'#{tc} {cnt_row} {cnt_col}')