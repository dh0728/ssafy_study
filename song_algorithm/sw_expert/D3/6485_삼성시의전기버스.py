# 1   //테스트 케이스 개수
# 2   //첫 번째 테스트 케이스, N=2
# 1 3 // A1 = 1, B1 = 3
# 2 5 // A2 = 2, B2 = 5
# 5   // P = 5
# 1   // 이하 C1 = 1, C2 = 2, C3 = 3, C4 = 4, C5 = 5
# 2
# 3
# 4
# 5


T = int(input())
for tc in range(1,T+1):
    N=int(input())  # N 버스노선의 수
    bus_list=[]
    counts = [0] *5001
    for n in range(1,N+1):
        A, B = (map(int, input().split())) # 버스노선 A이상 B이하
        for i in range(A,B+1):             # 다니는 버스 노선 count[i]=1
            counts[i] += 1
    P=int(input())  # 몇개의 버스가 다니는지 알고 싶은 버스정류장 갯수
    p_list=[]       # 몇개의 버스가 다니는지 알고 싶은 버스 정류장의 번호
    for n in range(P):  # 예시 p_list=[1,2,3,4,5]
        p_list.append(int(input()))
    result=[]
    for p in p_list: # 예시 p= 1 ,2 ,3 ,4 ,5
        result.append(counts[p]) # 결과리스트에 해당 리스트에 다니는 버스 수를 삽입
    print(f'#{tc}', ' '.join(map(str, result)))
