T=int(input())
for i in range(T):
	a = list(map(int, input().split()))
	if a[0] > a[1]:
		print(f'#{i+1} >')
	elif a[0] == a[1]:
		print(f'#{i+1} =')
	else:
		print(f'#{i+1} <')