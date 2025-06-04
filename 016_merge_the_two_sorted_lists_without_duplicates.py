# def merge(a,b,c):
#     print("1",c)
#     print("1.1",type(c))
#     x = set(c)
#     print("2",x)
#     print ("2.1",type(x))
#     print ("3",list(c))
#     print ("3.1",type(c))
#     return a,b,c
# a = [1,2,3,4,5,6]
# b = [2,5,8,7,9,3]
# c = a+b
# a,b,c = merge(a,b,c)

def merge(a,b):
    for i in b:
        if i not in a:
            a.append (i)
    return(a)
a = [1,2,3,4,5,6]
b = [5,6,7,8,9,10]
a = merge(a,b)
print ( a )
print(type(a))
