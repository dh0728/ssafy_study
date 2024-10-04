import sys
sys.stdin = open('input.txt')


K_li = [int(input()) for _ in range(9)]

for i in range(len(K_li)):
    for j in range(i+1, len(K_li)):
        if sum(K_li) - (K_li[i] + K_li[j]) == 100:
            x = K_li[i]
            y = K_li[j]

K_li.remove(x)
K_li.remove(y)

K_li.sort()
for i in K_li:

    print(i)