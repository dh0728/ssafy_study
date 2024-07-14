# 버전2
def sum_f(a,b,li1,li2): #a큰거
    r=0
    for i in range(0,a-b+1):
            sum=0
            for j in range(0, b):
                sum+=li1[j]*li2[i+j]
            if sum>r:
                r=sum
    return r

T = int(input())
for test_case in range(1,T+1):
    result=0
    N,M=map(int,input().split())
    li1=list(map(int,input().split()))
    li2=list(map(int,input().split()))
    if N<M:
        result=sum_f(M,N,li1,li2)
    elif N>M:
        result=sum_f(N,M,li2,li1)
    else:
        sum=0
        for i in range(0, N):
            sum+=li1[i]+li2[i]
    print(f"#{test_case} {result}")


