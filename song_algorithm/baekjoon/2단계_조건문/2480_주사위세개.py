li=list(map(int, input().split()))
num_set=list(set(li))

if len(num_set) == 3:
  num=sorted(num_set)[-1]
  print(num*100)
elif len(num_set) == 2:
  not_num=[]
  num = []
  for i in li:
    if i not in not_num:
      not_num.append(i)
    else:
      if i not in num:
        num.append(i)
  print(1000+num[0]*100)
else:
  print(10000 + num_set[0]*1000)

# 버전2
a, b, c = map(int, input().split())

if (a==b==c):
    print(10000+a*1000)
elif (a==b or b==c or c==a):
    if (a==b):
        print(1000+a*100)
    elif (b==c):
        print(1000+b*100)
    else:
        print(1000+c*100)
else:
    print(max(a,b,c)*100) 

# 버전 3
a,b,c=sorted(map(int,input().split()))
print(b==c)
print([c*100,1000+b*100,10000+a*1000][(a==b)+(b==c)])

# 버전 4
a,b,c=map(int,input().split())
if a==b==c:
  print(10000+1000*a)
elif a==b or a==c:
  print(1000+100*a)
elif b==c:
  print(1000+100*c)
else:
  print(100*max(a,b,c))