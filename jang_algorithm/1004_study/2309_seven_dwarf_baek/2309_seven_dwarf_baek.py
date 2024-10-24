import sys
sys.stdin = open('input.txt', 'r')

tall_lst = []
for _ in range(9):
    tall_lst.append(int(input()))
tall_lst.sort()
sum_t = sum(tall_lst)
print(tall_lst)


# asdf
# for i in range(len(tall_lst)):
#     for j in range():