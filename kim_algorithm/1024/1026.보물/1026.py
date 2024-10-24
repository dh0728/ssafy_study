import sys
sys.stdin = open('input.txt')

'''
A배열에서 제일 작은수, B배열에서 가장 큰  수를 곱하고 그다음 작은수와 큰수~~


'''

N = int(input())
A_li = list(map(int,input().split()))
B_li = list(map(int,input().split()))


A_li.sort() # A_li 오름차순 정렬

result = 0

for i in range(N): 
    result += A_li[i] * max(B_li)   # B_li에서 가장 큰 수, A_li에서 가장 작은 수 곱한 값 result에 넣기
    B_li.remove(max(B_li))  # B_li 에서 가장 큰 값 제거 


# N만큼 반복 

print(result)
