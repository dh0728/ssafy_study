import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    # 오, 아래, 왼, 오, 앞, 뒤
    dxyz=[[1,0,0],[0,1,0],[-1,0,0],[0,-1,0],[0,0,1],[0,0,-1]]
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    
    q=deque()

    # 익은 토마트 좌표 큐에 모조리 넣기
    for z in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[z][i][j] == 1:  # 익어있는 상태의 토마토면 큐에 넣기
                    q.append([z, i, j, 0])  # 현재 토마토 좌표, 날짜
                    visited[z][i][j] = 1

    max_days=0
    while q:
        z,i,j,days=q.popleft()
        max_days=days # 마지막 days가 다 익는데 걸리는 일수
        for dx,dy,dz in dxyz:
            ni= i+dx
            nj= j+dy
            nz= z+dz
            if ni<0 or ni>=N or nj<0 or nj>=M or nz<0 or nz>=H: #범위 벗어나면
                continue
            if visited[nz][ni][nj]: # 이미 방문했다면
                continue
            if tomato[nz][ni][nj]==-1: #토마토가 없는 칸이면 패스
                continue
            if tomato[nz][ni][nj]==0:   # 인접한 곳에 안익은 토마토 발견하면
                visited[nz][ni][nj]=1   # 방문처리
                tomato[nz][ni][nj] = 1  # 익은 토마토로 바꾸기
                q.append([nz,ni,nj,days+1]) # 큐에 넣기
    return max_days

def exam_tomato(): # 안익은 토마토가 있는지 검사
    global result
    for z in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[z][i][j] == 0: #안익은 토마토 있으면
                    result =-1  # -1 삽입
                    return


# M : 상자 가로칸, N: 세로, H: 높이
M,N,H=map(int,input().split())

# 1 = 익은 토마토 , 0 = 익지 않은 토마토 , -1 토마토 X
tomato=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

result=bfs()
exam_tomato() # 안익은 토마토 있는지 검사하기
print(result)