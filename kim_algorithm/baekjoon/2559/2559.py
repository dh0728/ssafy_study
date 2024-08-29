import sys
sys.stdin = open('input.txt')

N, K = map(int,input().split())
# N 온도측정 날짜 수, K 합을 구하기 위한 연속적인 날짜의 수
arr = list(map(int, input().split()))

'''
연속적인 k일의 온도 합 최대
'''


S = []
S.append(sum(arr[:K]))

for i in range(N-K):
    S.append(S[i] - arr[i] + arr[K+i])

print(max(S))

