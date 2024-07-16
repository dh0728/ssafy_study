# T = int(input())
# li=[]
# for i in range(5):
#   li.append(list(map(int, input().split())))

# for i in range(len(li)):
#   print(sum(li[i]))

import sys
N = int(sys.stdin.readline().rstrip())
N = int(input())
S = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    S.append(a+b)
for i in range(len(S)):
    print(S[i])