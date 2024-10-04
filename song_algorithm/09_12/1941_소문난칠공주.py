def dfs(depth,coords,Y_cnt,S_cnt):
    global cnt
    if Y_cnt >= 4: # 임도연파가 과만수 이상이면 pass
        return
    if depth==7: # 이다솜파가 과반수 이상이고 7명 모두 정해지면
        coords.sort() # 좌표들 정렬
        new_coords = tuple(coords) # 튜플로 변환
        if new_coords not in can_set: # 이미 전에 나온적 없는 경우에 수라면
            cnt+=1
            can_set.add(new_coords)

        # 바로 넣으면 시간초과??
        # can_set.add(new_coords) # set은 중복 불가능해서 그냥 다 넣어보기
        return

    for coord in coords: 
        x,y= coord[0], coord[1]
        for dx, dy in dxy:
            ni = x + dx
            nj = y + dy
            if ni < 0 or ni >= 5 or nj < 0 or nj >= 5: # 범위 벗어나면 pass
                continue
            if (ni,nj) in coords: # 이미 coords에 있는 좌표면 방문한 곳
                continue
            if arr[ni][nj] == 'Y':
                dfs(depth+1,coords+[(ni,nj)],Y_cnt+1,S_cnt)
            else:
                dfs(depth+1,coords+[(ni,nj)],Y_cnt,S_cnt+1)

arr=[list(input()) for _ in range(5)]
cnt=0
can_set=set()

dxy=[[0,1],[1,0],[0,-1],[-1,0]]
for i in range(5):
    for j in range(5):
        if arr[i][j]=='Y':
            dfs(1,[(i, j)], 1, 0) # 선택한 학생 개수(depth),현재좌표(coord), Y_cnt, S_cnt
        else:
            dfs(1,[(i, j)], 0, 1)
# print(len(can_set))
print(cnt)