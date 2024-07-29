T= int(input())
for i in range(T):
    a,b = list(map(int,input().split()))
    a_ = a // b
    b_ = a % b
    print(f'#{i+1} {a_} {b_}')