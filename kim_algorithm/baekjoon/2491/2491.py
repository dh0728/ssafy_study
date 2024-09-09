import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

'''
연속해서 커지거나(같은거포함)
연속해서 작아지는(같은거포함)
수열 중 길이가 가장 긴 것 출력

'''
in_cnt = 1         # 길이를 구할 (카운팅할) 변수
de_cnt = 1
max_len = 1     # 출력할 변수

# 연속해서 커지는 수열
for i in range(1, N):
    if arr[i] >= arr[i-1]:
        in_cnt += 1
    else:
        in_cnt = 1     # 변수 초기화
    if max_len < in_cnt:
        max_len = in_cnt

# 연속해서 작아지는 수열
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        de_cnt += 1
    else:
        de_cnt = 1
    if max_len < de_cnt:
        max_len = de_cnt
print(max_len)




