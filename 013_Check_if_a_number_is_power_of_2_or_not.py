# def power(f,e):
#     for i in range (f, e):
#         # print(i, end="-")
#         square = 2 ** i
#         # print(square, end=" ")
#         # k.append(square)
# f = 1
# e = 1000
# k = []
# power(f,e)
# # print()
# # print(k)
# # print()
# j = int(input("enter some value:"))
# if j in k:
#     print ( "it is power of 2: True" )
# else:
#     print ( "it is not power of 2: False" )

n = int(input("value: "))
if n > 0 and (n & (n - 1)) == 0:
    print("It is power of 2: True")
else:
    print("It is not power of 2: False")

