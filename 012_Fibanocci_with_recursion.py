# n = int(input("enter a value: "))
# x = []
# if n == 1:
#     x = [0]
#     print(x)
# elif n == 2:
#     x = [0,1]
#     print(x)
# elif n > 2:
#     x = [0,1]
#     while len(x) < n:
#         x.append(x[-1]+x[-2])
#     print(x)

def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
n = int(input("Enter a value: "))
fib_sequence = [fib_rec(i) for i in range(n)]
print(fib_sequence)
