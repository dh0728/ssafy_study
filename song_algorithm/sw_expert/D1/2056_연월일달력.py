T= int(input())
for test_case in range(1,T+1):
  case = input()
  Y = case[:4]
  M = case[4:6]
  D = case[6:8]
  if 1 <= int(M) <= 12:
    if M=='02' and int(D)>28:
      print(f'#{test_case} -1')
    elif (M=='01' or M=='03' or M=='05' or M=='07' or M=='08' or M=='10' or M=='12') and int(D) > 31:
      print(f'#{test_case} -1')
    elif (M=='04' or M=='06' or M=='09' or M=='11' or M=='08' or M=='10' or M=='12') and int(D) > 30:
      print(f'#{test_case} -1')
    else:
      print(f'#{test_case} {Y}/{M}/{D}')
  else:
    print(f'#{test_case} -1')

