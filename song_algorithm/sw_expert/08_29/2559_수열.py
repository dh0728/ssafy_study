# N, K=map(int,input().split()) 
# # N 온도를 측정한 전체 날짜 수, K 합을 구하기 위한 연속적인 날짜 

# arr=list(map(int,input().split()))

# max_sum= -100*K

# #시간초과 개화나네..
# for i in range(N-K+1): # 총 순회 횟수= N-K+1
#     sum_n=0            # 한 연속사이클 계산시마다 0으로 초기화
#     for j in range(i,i+K):  # i부터 연속하는 K일까지 온도순회
#         sum_n+=arr[j]  # 합 더하기
#     if max_sum < sum_n:
#         max_sum = sum_n
# print(max_sum)

# 누적합을 써야한단다
# 일반적으로  사용되는 배열에 값을 저장하고 지정된 인덱스부터 하나씩 더해가는 
# 방식은 최악의 경우O(n^2)의 시간복잡도를 갖기 때문에 입력의범위가 클 때 사용할 수 없다

# 다시 푼거
N, K=map(int,input().split()) 
# N 온도를 측정한 전체 날짜 수, K 합을 구하기 위한 연속적인 날짜 

arr=list(map(int,input().split()))

sum_n=0
for i in range(K): # 처음 연속되는 구간을 초기 최대 온도합으로 잡기
    sum_n+=arr[i]
max_sum=sum_n

# 처음 연속되는 구간을 제외한 만큼 반복 
# 예시)10일이면 총 9번인데 제일 처음 온도합을 제외하고 8번만 계산해서 비교
for i in range(N-K): 
    sum_n=sum_n -arr[i] + arr[i+K] # 전에 온도합구간에서 - 제일 앞에 날짜  + 겹치지 않는 다음 날짜  
    if sum_n > max_sum:
        max_sum=sum_n

print(max_sum)


# 다른 사람 풀이
result =[]

N, K = map(int,input().split())
a = list(map(int, input().split()))

for i in range(N - K + 1):
    result.append(sum(a[i:i+K]))
        
print(max(result))