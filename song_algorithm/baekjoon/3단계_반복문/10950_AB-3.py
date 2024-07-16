T= int(input())
li=[]
for i in range(T):
  li.append(list(map(int,input().split())))

for i in range(len(li)):
  print(sum(li[i]))

