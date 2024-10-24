import sys
sys.stdin = open('input.txt')

# 필요한 감독관 수의 최솟값을 구하는 프로그램 작성

N = int(input())    # 시험장 개수
Ai = list(map(int,input().split())) # 각 시험장에 있는 응시자 수
B, C = map(int,input().split()) # 총감독관 감시할 수 있는 응시자수 B, 부감독관 감시가능 수 C

# 총감독관은 반드시 1명 필요


cnt = N     # 총감독관의 수  = 시험장 개수 
for i in Ai:    
    i -= B      # 총감독관이 감시할 수 있는 응시자 수를 제외하고 남은 응시자 수 계산
    if i > 0: # 남은 응시자가 있을 경우에만 부감독관이 필요
        if i % C: # 남은 응시자를 부감독관이 모두 감시할 수 없으면
            cnt += (i//C) +1    # 부감독관이 모두 감시할 수 없는 경우에는 한 명을 추가
        else:   
            cnt += i//C # 딱 맞아떨어질 경우에는 부감독관이 추가적으로 딱 맞게 감시할 수 있음

print(cnt)


