def num(n):
    if n > 0:
        num(n - 1)
        print (n , end = " ")
    elif n > 100:
        print ("please enter some below 100 number")
n = int(input("enter the number below 100:"))
num(100)