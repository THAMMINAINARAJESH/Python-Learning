l = [1 , 22 , 45 , 3 , 22 , 8 , 22 , 22, 8 , 45 , 22 , 22 , 45 , 4 , 2 , 9]
empty = []
for i in l:
    count = 0
    for j in l:
        if i ^ j == 0:
            count += 1
    if count == 1:
        empty.append(i)
print(empty)