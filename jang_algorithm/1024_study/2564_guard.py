import sys
input = sys.stdin.readline

# 북쪽 모서리 0으로 잡고 펼쳤을 때 0으로부터 얼마나 떨어져있는지 계산해주는 함수(시계방향)
def cal_dist(loc, distance):
    if loc == 1: # 북쪽
        return distance
    elif loc == 4:  # 동쪽
        return w+distance
    elif loc == 2:  # 남쪽
        return w+h+w-distance
    elif loc == 3:  # 서쪽
        return w+h+w+h-distance
    
# 블록의 가로길이, 세로길이 입력받기
w, h = map(int, input().split())

# 상점의 개수
n = int(input())

# 상점 위치 저장할 리스트
dist = []

# 0에서부터 각 상점의 위치와 동근이 위치 입력받기
for i in range(n+1):
    loc, distance = map(int, input().split())
    dist.append(cal_dist(loc, distance))

# 동근이 0에서부터 떨어진 위치 저장
dong_dist = dist[-1]  # 마지막이 동근이 위치

answer = 0
for i in range(n):
    # 0에서 떨어진 각 가게의 거리, 0에서 떨어진 동근이 위치 차이 절댓값 구하기
    cal_distance = abs(dist[i]-dong_dist)

    # 전체길이
    total = 2*(w+h)

    # 더 작은 값 answer에 할당
    answer += min(cal_distance, total-cal_distance)

print(answer)