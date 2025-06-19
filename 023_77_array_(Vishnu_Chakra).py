def mat(n):
    mat = [[0] * n for _ in range (n)]
    top , bottom , left , right = 0 , n - 1 , 0 , n - 1
    num = 1
    while top <= bottom and left <= right :
        for i in range (left , right + 1):
            mat [top] [i] = num
            num += 1
        top += 1
        for i in range (top , bottom + 1):
            mat [i] [right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for i in range (right , left -1 , -1):
                mat [bottom] [i] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range (bottom , top -1 , -1):
                mat [i] [left] = num
                num += 1
            left += 1
    return mat
n = int(input("enter some value : "))
result = mat(n)
for row in result:
    print(*row)
