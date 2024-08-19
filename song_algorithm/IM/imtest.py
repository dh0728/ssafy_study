import sys
sys.stdin=open('input.txt')

def ch_led(n):  # 상태변하게 해주는 함수
    for i in range(n,N+1,n):
        if led[i]==1:
            led[i]=0
        else:
            led[i]=1

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    led=[0]*(N+1)
    cnt=0

    for i in range(N): #처음꺼부터 비교
        if arr == led: #같아지면 break
            print(1)
            break
        if arr[i] != led[i+1]:
            ch_led(i+1)
            # print(led)
            cnt +=1

    print(f'#{tc} {cnt}')