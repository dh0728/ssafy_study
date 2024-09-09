# 3키로와 5킬로 봉지를 이용해 최소한의 봉지로 배달해야한다.
# 정확하게 N 킬로그램을 만들 수 없다면 -1 출력
N=int(input()) # 배달해야하는 소금 무게 kg

# kg_list에 kg 순서가 큰 순서대로 있으면 깊이 탐색시
# 무조건 큰 무게로 했을 때로 깊이 탐색하고 점점 가벼운
# 무게의 설탕을 추가해서 봉지수를 계산하므로 처음 계산된
# 봉지수가 결국 최소 봉지 수 따라서 한번 봉지수가 지정되면 실행 X
def dfs(cnt,n):
    global result
    if result != -1: # 한번 봉지수가 계산되면 그게 최소 봉지수
        return       # 이후 과정은 그냥 바로 리턴
    if n<0:  # 정확하게 안만들어지면 리턴
        return
    if n==0: # 봉지를 다선택하면
        result=cnt # result에 봉지수 삽입
        return
    for kg in kg_list:
        dfs(cnt+1,n-kg)
    return
kg_list=[5,3]
result=-1 # 처음엔 만들수 없는 경우인 -1로 초기화
dfs(0,N)
print(result)

# 시간 초과 난 풀이
N=int(input()) # 배달해야하는 소금 무게 kg

# 3키로와 5킬로 봉지를 이용해 최소한의 봉지로 배달해야한다.
# 정확하게 N 킬로그램을 만들 수 없다면 -1 출력
def dfs(cnt,n):
    global result
    if n<0:
        return
    if cnt >=result: # 봉지 수가 처음 계산된 최소 봉지 수보다 커지면 바로 계산 중지
        return
    if n==0: # 봉지를 다선택하면
        result=cnt
        return
    for kg in kg_list:
        dfs(cnt+1,n-kg)
    return
kg_list=[5,3]
result=1000 # N에 최대 범위일때의 나올수 있는 최소 봉지수로 초기화
dfs(0,N)
if result==1000: # 정확하게 만들수 없는 경우
    print(-1)
else:            # 정확하게 만들어지는 경우
    print(result)
