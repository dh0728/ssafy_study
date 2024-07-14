#버전 1
T = int(input())
for test_case in range(1, T + 1):
    result = 0
    N,M=map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    if N < M:
        for i in range(0, M-N+1):
            sum = 0
            for j in range(0, N):
                sum += list1[j]*list2[i+j]
            if sum > result:
                result = sum
    elif N > M:
        for i in range(0, N-M+1):
            sum = 0
            for j in range(0, M):
                sum += list2[j]*list1[i+j]
            if sum > result:
                result = sum
    else:
        sum=0
        for i in range(0, N):
            sum += list1[i]+list2[i]
    print(f"#{test_case} {result}")


