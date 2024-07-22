H, M = map(int,input().split())

if H!=0 and M < 45 :
    print(f'{H-1} {M+15}')
elif H!=0 and M >=45 :
    print(f'{H} {M-45}')
elif H == 0 and M <45 :
    print(f'{H+23} {M+15}')
elif H == 0 and M >=45 :
    print(f'{H} {M-45}')
