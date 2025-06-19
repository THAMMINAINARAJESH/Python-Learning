arr = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
print(arr)
n = int(input("enter a number to find:"))
low = 0
high = len(arr) - 1
flag = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == n:
        flag = True
        break
    elif arr[mid] < n:
        low = mid + 1
    elif arr[mid] > n:
        high = mid - 1
if flag == True:
    print("element found:", [mid])
else:
    print("element not found.")