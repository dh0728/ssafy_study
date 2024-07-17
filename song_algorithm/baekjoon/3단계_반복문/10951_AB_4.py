while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
    
import sys
for line in sys.stdin.readlines():
    print(sum(map(int, line.split())))

# sys.stdin 을 사용하는 이유(input 말고)
# input()을 사용했을 때는 시간 초과가 발생 할 수 있다. 
# 사용법 

# 한 개의 정수를 받을 때
# a = int(sys.stdin.readline())

# 정해진 개수를 한 줄에
# a,b,c = map(int,sys.stdin.readline().split())

# 임의의 개수의 정수를 한줄에 받고 리스트에 저장
# data = list(map(int,sys.stdin.readline().split()))

# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
# import sys
# data = []
# n = int(sys.stdin.readline())
# for i in range(n):
#     data.append(list(map(int,sys.stdin.readline().split())))

# 문자열 n줄을 입력받아 리스트에 저장
# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]

# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

