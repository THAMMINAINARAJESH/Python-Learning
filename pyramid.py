n = int(input("enter a value: "))
def print_pyramid(n):
    value = 1
    for i in range (1 , n + 1):
        print(" " * (n - i) , end = " ")
        for j in range (i):
            print(value , end = " ")
            value = value + 1
        for k in range (i - 1):
            print(value , end = " ")
            value = value + 1
        print()
print_pyramid(n)