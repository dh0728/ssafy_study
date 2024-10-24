from collections import deque

n = int(input())

# 방법 1 - 일반적인 for문
# arr = []
# for _ in range(n):
#     a = list(map(int, input()))
#     arr.append(a)

# 방법 2 - 리스트 컴프리헨션
arr1 = [list(map(int, input())) for _ in range(n)]

