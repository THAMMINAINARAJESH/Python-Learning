a = str("dhcedhicqeiucb")
b = str("")
for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
    if count < 2:
        break
print(i)

