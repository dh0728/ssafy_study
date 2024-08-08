import sys
sys.stdin = open("우주선_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    dij = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    arr = [list(map(int, input().split())) for _ in range(N)]

    A = 0

    for i in range(0, N):
        for j in range(0, M):
            spot = arr[i][j]
            counts = 0
            for di, dj in dij:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                if spot > arr[ni][nj]:
                    counts +=1
            if counts >= 4:
                A +=1

    print(f'#{test_case} {A}')

    # import sys
    #
    # sys.stdin = open("반복_input.txt")
    #
    # T = int(input())
    # for test_case in range(1, T + 1):
    #     arr = input()
    #     stack = []
    #     for i in range(len(arr)):
    #         if len(stack) != 0 and stack[-1] == arr[i]:
    #             stack.pop()
    #         else:
    #             stack.append(arr[i])
