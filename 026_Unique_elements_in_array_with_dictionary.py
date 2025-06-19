l = [1 , 22 , 45 , 3 , 22 , 8 , 22 , 22, 8 , 45 , 22 , 22 , 45 , 4 , 2 , 9]
D = { }
for i in range (len(l)):
    if l[i] in D:
        D [ l [ i ] ] += 1
    else:
        D [ l [ i ] ] = 1
for j in D:
    if D [ j ] == 1:
        print({j:0} , end = " ")