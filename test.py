
for tc in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    B = []
    A = []
    for i in range(2,N-2):
        a = height[i] > height[i-2]
        b = height[i] > height[i-1]
        c = height[i] > height[i+2]
        d = height[i] > height[i+1]
        if a and b and c and d == True:
            A.append(height[i-2:i+3]) 
    C = []
    for j in A:
        C.append(sorted(j)[-1] - sorted(j)[-2])
    print(f'#{tc} {sum(C)}')