n = int ( input ( "Enter number of rows: " ) )
width = len ( str (n * (2 * n - 1)) // 2 ) + 1
def print_diamond(n):
    value = 1
    for i in range ( 1, n + 1 ):
        print ( " " * width * (n - i), end="" )
        for j in range ( i ):
            print ( f"{value:>{width}}", end="" )
            value += 1
        for k in range ( i - 1 ):
            print ( f"{value:>{width}}", end="" )
            value += 1
        print ()
    for i in range ( n - 1, 0, -1 ):
        print ( " " * width * (n - i), end="" )
        for j in range ( i ):
            print ( f"{value:>{width}}", end="" )
            value += 1
        for k in range ( i - 1 ):
            print ( f"{value:>{width}}", end="" )
            value += 1
        print ()
print_diamond ( n )
