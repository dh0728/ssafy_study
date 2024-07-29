T = int(input())

for i in range(T):
	A = []
	numbers =  list(map(int,input().split()))
	for x in numbers:
		if x % 2 != 0:
			A.append(x)
	summ=sum(A)
	print(f'#{i+1} {summ}')