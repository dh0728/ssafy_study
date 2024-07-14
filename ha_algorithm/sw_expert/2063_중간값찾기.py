N = int(input())
score = list(map(int, input().split()))
score.sort()
mid = N // 2
median = score[mid]
print(median)