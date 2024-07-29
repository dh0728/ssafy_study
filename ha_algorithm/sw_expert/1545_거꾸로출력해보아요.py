t = int(input())
a = []
for i in range(t+1):
    a.append(i)
b = []
for x in range(len(a)):
    c = a.pop()
    b.append(c)
print(' '.join(map(str,b)))