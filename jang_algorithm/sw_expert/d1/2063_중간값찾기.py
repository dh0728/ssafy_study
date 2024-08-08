N = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
mid = N // 2
print(numbers[mid])