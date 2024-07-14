def rotation(ls, N):
    dic={0:ls} 
    for a in range(1,4):
        ro_ls = []
        for i in range(0, N):
            ro_arr = []
            for j in range(N-1, -1, -1):
                ro_arr.append(dic[(a-1)*90][j][i])
            ro_ls.append(ro_arr)
        dic[a*90]=ro_ls
    return dic

T = int(input())
for test_case in range(1,T + 1):
    N =int(input())
    ls=[]
    for i in range(0,N):
        ls.append(list(map(int,input().split())))
    result= rotation(ls, N)
    print(f"#{test_case}")
    for i in range(0, N):
        for r in range(1,4): 
            for j in range(0,N):
                print(result[90*r][i][j], end="")
                if j==N-1:
                    print(" ",end="")
            if r==3:
                print(" ")