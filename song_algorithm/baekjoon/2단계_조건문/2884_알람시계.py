H,M=map(int,input().split())
new_min=M-45

if new_min < 0 and H>0:
  print(f'{H-1} {60+new_min}')
elif new_min == 0 and H>0:
  print(f'{H} 0')
elif new_min > 0 and H>0:
  print(f'{H} {new_min}')
elif new_min < 0 and H == 0:
  print(f'23 {60+new_min}')
elif new_min > 0 and H == 0:
  print(f'0 {new_min}')
else:
  print('0 0')

# 방법2 
total = H * 60 + M -45
if total < 0:
  total += 60 * 24 
H = total // 60
M = total % 60
print(H,M)