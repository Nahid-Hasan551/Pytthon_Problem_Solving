array = [1, 2, 3, 4, 5, 6, 7, 8]

temp = array[0]
array[0] = array[-1]
array[-1] = temp
print("After swapping", array)


