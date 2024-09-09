def count_sum():    
    cnt=0
    for i in range(101):
        for j in range(101):
            if map[i][j]:   # 맵 다보면서 1인 부분 체크
                cnt+=1
    return cnt

def check_square(sq):
    x1,y1,x2,y2=sq[0],sq[1],sq[2],sq[3] 
    for j in range(x1,x2):      # 왼쪽 아래 꼭짓점 x 에서 오른쪽 위 꼭짓점 x까지
        for i in range(y1,y2):  # 왼쪽 아래 꼭짓점 y 에서 오른쪽 위 꼭짓점 y까지
            map[i][j]=1         # 1로 색칠

arr=[list(map(int,input().split())) for _ in range(4)]
map=[[0]*101 for _ in range(101)]   
for a in arr:
    check_square(a) #색칠함수 호출

result=count_sum()  #색칠한 부분 카운트
print(result)