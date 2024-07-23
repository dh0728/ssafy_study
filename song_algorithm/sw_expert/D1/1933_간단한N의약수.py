N=int(input())
li=[]
for i in range(1, N//2):
    if N%i ==0 and i not in li:
        li.extend([i,int(N/i)])
li.sort()
for l in li:
    print(l,end=' ')