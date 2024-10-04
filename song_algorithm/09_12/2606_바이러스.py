from collections import deque
def bfs(node):
    global cnt
    visited = [0] * (N + 1)
    q=deque()
    q.append(node)
    visited[node]=1
    while q:    # 큐에 값이 있을 동안만 반복
        n = q.popleft()
        for next_n in graph[n]: # 다음 노드 탐색
            if visited[next_n]: # 이미 방문한 노드는 pass
                continue
            cnt+=1              # 새로운 노드찾으면 감염 node 카운팅 +1
            visited[next_n]=1   # 방문처리
            q.append(next_n)    # 큐에 삽입
    return

N=int(input()) # 노드수
M=int(input()) # 간선수
arr=[list(map(int,input().split())) for _ in range(M)] # 간선 정보

graph=[[] for _ in range(N+1)]
for a in arr:
    graph[a[0]].append(a[1])
    graph[a[1]].append(a[0])

visited=[0]*(N+1)
cnt=0
bfs(1)
print(cnt)
