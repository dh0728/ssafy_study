'''
1. 다리는 항상 직선이다.
2. 동일한 좌표 셀을 중복 가능(겹치기 가능)
3. 출력 -> 다리 길이의 최소 합
4. 0은 바다, 1은 육지(섬)
'''

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    jido = [list(map(int, input().split())) for _ in range(N)]

    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for i in range(N):
        for j in range(N):
            if jido[i][j] == 0 or 3: continue
            for dx, dy in dxy:
                n_island = []
                ni = i + dx
                nj = j + dy
                if 0<=ni<N and 0<=nj<N and jido[ni][nj]==0:
                    while jido[ni][nj] == 0:
                        ni += dx
                        nj += dy
                    print(ni,nj)



