import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


# 정열 쓴 풀이
A.sort()
B.sort(reverse=True)

result=0
for i in range(N):
    result += A[i]*B[i]

print(result)

# 정렬 안쓴 플이 
result=0

for i in range(N):
    max_A=max(A) # A에서 제일 큰값
    min_B=min(B) # B에서 제일 큰값
    result += max_A * min_B
    A.pop(A.index(max_A))
    B.pop(B.index(min_B))

print(result)
