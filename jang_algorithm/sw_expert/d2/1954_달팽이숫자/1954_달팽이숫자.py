import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()