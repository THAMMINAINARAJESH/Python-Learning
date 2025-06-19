n = int(input("enter some number:"))
def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
for i in range (0 , n+1):
    c = i, fib_rec(i)
    print(c , end = " ")