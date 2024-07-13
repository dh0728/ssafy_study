def dir_list(i,j,dx,dy): 	#파리수 세는 함수 만들기
    count = arr[i][j]
    for a in range(4):
        for b in range(1, M):
            x = i + dx[a] * b
            y = j + dy[a] * b
            if x < 0 or y < 0 or x >= N or y >= N: #x,y는 리스트의 x,y크기보다 크지 않을 경우 더하기
                continue
            count +=arr[x][y]
    return count

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr =[]
    for i in range(N):
        arr.append(list(map(int, input().split())))
    result=0
    plus_dx = [0, 0, -1, 1]  # 플러스 모양 x좌표이동 상하좌우순
    plus_dy = [-1, 1, 0, 0]  # 플러스 모양 y좌표이동 상하좌우순
    egs_dx = [-1, 1, -1, 1]  # 엑스 모양 x좌표이동
    egs_dy = [-1, 1, 1, -1]  # 엑스 모양 y좌표이동
    for i in range(0, N):
        for j in range(0, N):
            plus = dir_list(i , j , plus_dx , plus_dy)
            if plus > result:
                result=plus
            egs = dir_list(i , j , egs_dx , egs_dy)
            if egs > result:
                result=egs
    print(f"#{test_case} {result}")