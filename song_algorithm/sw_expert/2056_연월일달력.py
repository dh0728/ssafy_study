T=int(input())

for test_case in range(1, T+1):
  N=input()
  year=N[:4]
  month=int(N[4:6])
  date=int(N[6:])
  if 1 > month > 12:
    print(f"#{test_case} -1")
  else:

