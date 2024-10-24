# 백준 2564 경비원

import sys
sys.stdin = open('input.txt')

garo, sero = map(int,input().split()) # 블록의 가로, 세로
store_num = int(input())    # 상점의 개수

# 상점의 위치 i: 위치방향, j: 동서 -> 위쪽으로부터거리/ 남북->왼쪽으로부터거리
    # 1 북쪽, 2 남쪽 3 서쪽 4 동쪽
for _ in range(store_num):
    store_current, store_distance = map(int,input().split())

dong_current, dong_distance = map(int,input().split())     # 동근이 위치

result = []     # 최단거리들을 담을 빈 리스트

def short_distance():
    global result

    if dong_current == store_current:
        result = abs(dong_distance-store_distance)
        return result

    elif dong_current != store_current:
        pass


