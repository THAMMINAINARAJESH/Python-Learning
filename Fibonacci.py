n = int(input("enter a value: "))
x = []
if n == 1:
    x = [0]
    print(x)
elif n == 2:
    x = [0,1]
    print(x)
elif n > 2:
    x = [0,1]
    while len(x) < n:
        x.append(x[-1]+x[-2])
    print(x)