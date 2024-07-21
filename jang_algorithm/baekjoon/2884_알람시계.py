H,M= map(int, input().split())
# H ,M = 1 , 2

if M - 45 <0:
    if H == 0:
        print(23,15+M)
    else:
        print(H-1, 15+M)

else:
    print(H, M-45)