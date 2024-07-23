for i in range(5):
    print(f'{"+"*(i)}{"#"}{"+"*(4-i)}')

#다른사람 방법
for i in range(5):
    plus = list("+++++")
    plus[i] = "#"
    print("".join(plus))