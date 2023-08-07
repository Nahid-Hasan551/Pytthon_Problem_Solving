arr = [1, 2, 3, 4, 5]
maximum = arr[0]
n = len(arr)
for i in range(1, n):
    if arr[i] > maximum:
        maximum = arr[i]
print("Maximum value of array: ", maximum)

arr2 = [1, 2, 3, 4, 5]
minimum = arr2[0]
n = len(arr2)
for i in range(1, n):
    if arr2[i] < minimum:
        minimum = arr2[i]
print("Minimum value of array:", minimum)
