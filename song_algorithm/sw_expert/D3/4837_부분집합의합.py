def dfs_find(v):
    global cnt
    if v==12 + 1:
        sum=0
        num_cnt=0
        for i in range(1, 12+1):
            if visited[i]==1:   # 부분집합이 원소 i를 가지는 경우
                sum+=i          # 부분집합의 합 업데이트
                num_cnt+=1      # 부분집합이 가지는 원소 카운트
                if num_cnt >N:  # 부분집합의 갯수가 6개 이상이면 break
                    break
                #print(i, end=' ')
        # print()
        if sum==K and num_cnt==N: # 부분집합의 갯수가 N개이고 합이 K이면 count+1
            cnt +=1
    else:
        visited[v]=1    
        dfs_find(v+1)
        visited[v]=0
        dfs_find(v+1)

T=int(input())
for tc in range(1,T+1):
    N, K=map(int, input().split())
    count=0     # N개의 원소를 가지고 합이 K인 부분집합의 갯수
    visited = [0] * (12 + 1) #visited의 index가 집합이 가지는 원소
    dfs_find(1)
    print(f'#{tc} {count}')

#빽트레킹 한거
def dfs_find(v, num, sum):
    global count
    if v > 12: # v 원소의 개수가 12개 이상 일시
        return
    if num >N:  # 원소 숫자가 N개 이상 return
        return
    if sum >K:  # 합이 K이상일시 return
        return
    if num==N and sum==K:   #num이 N이거나 sum==K이면 count+1
        count +=1           #만족하는 부분집합수 +1
        return
    visited[v]=1
    dfs_find(v+1,num+1, sum+v)
    visited[v]=0
    dfs_find(v+1, num, sum)

T=int(input())
for tc in range(1,T+1):
    N, K=map(int, input().split())
    count=0     # N개의 원소를 가지고 합이 K인 부분집합의 갯수
    visited = [0] * (12 + 1) #visited의 index가 집합이 가지는 원소
    dfs_find(1, num=0, sum=0)
    print(f'#{tc} {count}')

