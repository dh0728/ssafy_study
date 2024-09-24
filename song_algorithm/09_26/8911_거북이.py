import sys
input=sys.stdin.readline

def find_x_y(control):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]] # 위, 왼, 아래, 오 
    x,y=0,0
    angle=0 # 시작 방향 0:위 , 1:왼 , 2: 아래, 3: 오  => dxy의 인덱스와 동일하게
    x_set=set([0]) # 초기 좌표 넣기
    y_set=set([0])

    for c in control:
        if c=='L':                  # 왼쪽으로 회전
            angle=(angle+1)%4       # 각도 4 안넘어가게 4로 나눈 나머지로 넣기 
        elif c=='R':                # 오른쪽으로 회전
            angle=(angle-1)%4
        elif c=='F':                # 앞으로 한칸
            x = x + dxy[angle][0]   # 현재 보는 방향대로 좌표이동
            y = y + dxy[angle][1]
            x_set.add(x)
            y_set.add(y)
        else:                       # 뒤로 한칸 - 현재 보는 방향의 반대로 이동
            x = x + dxy[angle-2][0] # x -= dxy[angle][0] 그냥 빼도 되긴하네
            y = y + dxy[angle-2][1] # y -= dxy[angle][1] 
            x_set.add(x)
            y_set.add(y)

    return (max(x_set)-min(x_set)) * (max(y_set)-min(y_set))

T=int(input())
for tc in range(1,T+1):
    control_list=input().strip()
    result=find_x_y(control_list)
    print(result)

##------------------------------------------------------------------------------------

## set 안쓴 풀이
def find_x_y(control):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    x,y=0,0
    angle=0

    # set 안쓰고 풀려면 최대,최소 x,y 좌표값 변수로 저장
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0
    for c in control:
        if c=='L':
            angle=(angle-1)%4
        elif c=='R':
            angle=(angle+1)%4
        else:

            if c=='F': # 앞으로 한칸
                x += dxy[angle][0]
                y += dxy[angle][1]
            else: # 뒤로 한칸
                x -= dxy[angle][0]
                y -= dxy[angle][1]

            # 이동 할때 마다 갱신
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    return (max_x - min_x) * (max_y - min_y)