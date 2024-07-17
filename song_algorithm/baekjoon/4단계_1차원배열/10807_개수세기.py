N=int(input())
li=list(map(int,input().split()))
v=int(input())

count=0
for i in li:
  if i==v:
    count += 1

print(count)

#버전2
N = int(input())
nums = list(map(int,input().split()))
v = int(input())
print(nums.count(v))

#버전3

a = int(input())
list = input().split()
print(list)
print(list.count(input()))