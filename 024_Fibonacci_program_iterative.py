n = int(input("enter some value:")) # 0 , 1, 1 , 2 , 3 , 5 , 8
a = 0
b = 1
i = 0
while i < n:
    print (a , end = "  ")
    result = a + b
    b = a
    a = result
    i = i + 1