# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

# 정점, 간선수, 시작점을 입력받음
N, M, V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
# n+1을 사용하는 이유는 정점은 1~4까지이고, 0번째 인덱스를 사요하지 않기 위해서다.

# 연결된 정점을 입력
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# dfs와 bfs 그래프의 방문 여부를 담을 리스트
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

# dfs 알고리즘

def dfs(V):
    # 방문 처리
    visited1[V] = True
    # 방문 후, 정점 출력
    print(V, end=" ")
    # 방문 기록이 없고, 인덱스에 값이 있다면(연결되어있다면)
    for i in range(1, N+1):
        if not visited1[i] and graph[V][i] == 1:
            # 방문한다. 재귀함수 활용
            # 호출될 때마다 visited는 1이 되고 재귀되어 V에 i가 들어간다
            dfs(i)

# bfs 알고리즘

def bfs(V):
    # 방문할 곳을 순서대로 넣을 큐
    q = deque([V])
    # 방문 처리
    visited2[V] = True
    # 큐 안에 데이터가 없을 때 까지 실행됨
    while q:
        # 큐 맨 앞에 있는 값을 꺼내서 출력한다
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N+1):
            # 방문기록이 없고, 인덱스에 값이 있다면(연결되어있다면)
            if not visited2[i] and graph[V][i] == 1:
                q.append(i) # 큐에 추가한다.
                visited2[i] = True

dfs(V)
print()
bfs(V)