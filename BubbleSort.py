arr = [8, 9, 1, 5, 7, 0]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Sorted array:", arr)