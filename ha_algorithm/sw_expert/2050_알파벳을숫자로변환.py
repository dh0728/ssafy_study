t = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
convert_alpha = []
for i in t:
    i = alpha.index(i)+1
    convert_alpha.append(i)
print(" ".join(map(str,convert_alpha)))