def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("Iterasi ke-", i+1, ":", arr)

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Array awal:", arr)
bubble_sort(arr)
print("Array yang telah diurutkan:")
for i in range(len(arr)):
    print(arr[i])

