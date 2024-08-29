# 백준 - 직사각형 네개의 합집합의 면적 구하기

import sys
sys.stdin = open('input.txt')


arr = [[0]*101 for _ in range(101)]
result = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

    result = 0
    for lst in arr:
        result += sum(lst)

print(result)



