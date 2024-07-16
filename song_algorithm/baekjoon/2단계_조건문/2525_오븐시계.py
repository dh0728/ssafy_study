H , M=map(int, input().split())
C = int(input())

max = 1440 
total = H*60 + M + C
if total >= max:
  total-=max
h= total // 60
m= total % 60
print(f'{h} {m}')

