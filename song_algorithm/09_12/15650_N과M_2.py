
# 풀이 1
def find_sequence(cnt,seq):
    if cnt>=M:
        print(*seq)
        return
    for n in range(1,N+1):
        if select[n]:   # 이미 선택한 수열이면 pass
            continue    
        if n <= seq[-1]: # 전 숫자보다 작으면 pass
            continue
        select[n]=1 #  숫자 n 선택
        find_sequence(cnt+1,seq+[n])
        select[n]=0 # 다음 수열 생성을 위해 선택 확인 리스트 복원

# 1부터 N까지 중복없이 M개를 고른 수열
N,M=map(int,input().split())
select=[0]*(N+1)
for n in range(1,N+1): # 수열을 첫 숫자를 넣어 주면서 시작
    select[n] = 1 # 숫자 n 선택
    find_sequence(1,[n]) # 선택한 숫자 개수, 수열리스트
    select[n] = 0 # 다음 수열 생성을 위해 복원

# 풀이2
# 해당 숫자를 선택했는지 확인하는 과정을 아래코드로 바꿔서 생략가능
# if n <= seq[-1]: # 전 숫자보다 작으면 pass
#     continue
def find_sequence(cnt,seq):
    if cnt>=M: 
        print(*seq)
        return
    for n in range(1,N+1):
        if n <= seq[-1]: # 전 숫자보다 작으면 pass
            continue
        find_sequence(cnt+1,seq+[n])

# 1부터 N까지 중복없이 M개를 고른 수열
N,M=map(int,input().split())
select=[0]*(N+1)
for n in range(1,N+1): # 수열을 첫 숫자를 넣어 주면서 시작
    find_sequence(1,[n]) # 선택한 숫자 개수, 수열리스트
