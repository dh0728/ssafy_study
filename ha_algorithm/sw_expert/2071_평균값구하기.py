T = int(input())
for i in range(T):
    numbers = list(map(int,input().split()))
    B= sum(numbers)
    C = B/10
    print(f'#{i+1} {round(C)}')
        