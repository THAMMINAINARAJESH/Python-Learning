n = int(input("enter no of rows: "))
# def print_pyramid(n):
#     value = 1
#     for i in range (1 , n + 1):
#         print(" " * (n - i) , end = " ")
#         for j in range (i):
#             print(value , end = " ")
#             value = value + 1
#         for k in range (i - 1):
#             print(value , end = " ")
#             value = value + 1
#         print()
# print_pyramid(n)
width = len(str(n * (2 * n - 1) // 2)) + 1 
def print_pyramid(n):
    value = 1
    for i in range(1, n + 1):
        print(" " * width * (n - i), end="")
        for j in range(i):
            print(f"{value:>{width}}", end="")
            value += 1
        for k in range(i - 1):
            print(f"{value:>{width}}", end="")
            value += 1
        print()
print_pyramid(n)
