T= int(input())
for test_case in range(1,T+1):
  A,B = map(int, input().split())
  result=A/B
  print(f'#{test_case} ', end='')
  if result < 1:
    print('<')
  elif result > 1:
    print('>')
  else:
    print('=')

#버전2
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A,B=map(int,input().split())
    if A > B:
        print(f"#{test_case} >")
    elif A < B:
        print(f"#{test_case} <")
    else:
        print(f"#{test_case} =")