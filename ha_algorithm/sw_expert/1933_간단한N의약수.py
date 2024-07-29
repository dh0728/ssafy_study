t = int(input())
a =[]
for i in range(1,t+1):
    if t % i == 0:
        a.append(i)
print(' '.join(map(str,a)))