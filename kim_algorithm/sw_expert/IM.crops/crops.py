import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    M = N//2    # M을 중앙값으로 설정했을 때 N//2 와 동일한 값이 됨
    result = 0  # 수익 초기화

    for i in range(N):
        if i <= M:      # i = 행의 인덱스
            for j in range(M-i, M+i+1):
                result += arr[i][j]

        else:
            for j in range(i-M, N-(i-M)):
                result += arr[i][j]

    print(f'#{tc} {result}')

