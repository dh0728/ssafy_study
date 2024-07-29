t = int(input())
a = [1]
for i in range(1, t+1):
    b = a[i-1] *2
    a.append(b)
print(' '.join(map(str,a)))
    