# a = str("123456")
# print(type(a))
# print(a)
# b = int(a)
# print(type(b))
# print(b)


def function(a,b):
    print ( type ( a ) )
    print ( a )
    print ( type ( b ) )
    print ( b )
    return(a,b)
a = str(input("enter some string values: "))
b = int(a)
a,b = function(a,b)

