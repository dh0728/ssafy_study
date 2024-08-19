import sys
sys.stdin = open("Gravity_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_A = 0
    for i in range(0, N-1):
        count = 0
        A = N - 1 -i     
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                count += 1
        A -=count
        if max_A < A:
            max_A = A

    print(f'#{test_case} {max_A}')