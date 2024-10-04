from collections import deque

# 칠공주가 인접하는지 확인할 bfs
def bfs(si, sj):
    q = deque()
    # 새로운 v 배열 생성
    visited_2 = [[0]*5 for _ in range(5)]

    q.append((si, sj))
    visited_2[si][sj] = 1
    cnt = 1
    # 네 방향 확인하면서 인접한지 체크
    dxy = [[0,1], [1, 0], [0, -1], [-1, 0]]
    while q:
        ci, cj = q.popleft()
        for dx, dy in dxy:
            ni = ci + dx
            nj = cj + dy
            # 4방향, 범위 내, 미방문, 칠공주인지 체크
            if 0<=ni<5 and 0<=nj<5 and visited_2[ni][nj] == 0 and visited[ni][nj] == 1:
                q.append((ni, nj))
                visited_2[ni][nj] = 1
                cnt += 1
    return cnt == 7 # cnt가 7이면 true

# 칠공주인지 체크할 시작 칸 찾기
def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j]==1:
                return bfs(i,j)

def dfs(n, cnt, s_cnt):
    global ans
    if cnt > 7:
        return

    # 끝 칸까지 오게 되면, 칠공주이며, 다솜파가 4명이상이다 -> 인접한 7명인지 체크 후 ans +1
    if n == 25:
        if cnt == 7 and s_cnt >= 4:
            if check():
                ans += 1
        return

    # 2차원 배열을 1차원으로 변환..
    visited[n//5][n%5] = 1 # 7명 학생에 포함하는 경우
    dfs(n+1, cnt+1, s_cnt+int(arr[n//5][n%5]=='S')) # int 괄호 내 저게 맞으면 +1, 아니면 +0
    visited[n//5][n%5] = 0 # 원상 복구
    dfs(n+1, cnt, s_cnt)   # 7명 학생에 포함하지 않는 경우


arr = [input() for _ in range(5)]
ans = 0
visited = [[0] * 5 for _ in range(5)]
# 학생번호(0~24), 포함학생 수, 다솜파 학생 수
dfs(0,0,0)
print(ans)
