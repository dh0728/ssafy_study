def rotation(arr, N):
    rotation_arr = []
    for i in range(0, N):
        bef_ro_arr = []
        for j in range(N-1, -1, -1):
            bef_ro_arr.append(arr[j][i])
        rotation_arr.append(bef_ro_arr)
    return rotation_arr

T = int(input())
for test_case in range(1, T + 1):
    N =int(input())
    arr = []
    for i in range(0,N):
        arr.append(list(map(int, input().split())))
    rotation90= rotation(arr, N)
    rotation180= rotation(rotation90,N)
    rotation270= rotation(rotation180,N)
    print(f"#{test_case}")
    for i in range(0, N):
        for j in range(0,N):
            print(rotation90[i][j], end="")
            if j==N-1:
                print(" ",end="")
        for j in range(0,N):
            print(rotation180[i][j], end="")
            if j==N-1:
                print(" ",end="")
        for j in range(0,N):
            print(rotation270[i][j], end="")
            if j==N-1:
                print(" ",end="\n") 