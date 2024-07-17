T=int(input())

for t in range(1, T+1):
    A, B = list(map(int, input().split()))
    print(f'Case #{t}: {A+B}')

#버전2
T=int(input())
li =[]
for t in range(T):
    li.append(list(map(int, input().split())))
for t in range(1, T+1) : 
    print(f'Case #{t}: {li[t-1][0]+li[t-1][1]}')