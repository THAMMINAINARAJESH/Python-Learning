a = [1,2,3,4,5,6,4,3,2,5,6,0,9,86,5,3]
b = []
for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
    if count < 2:
        b.append(i)
print(b)


