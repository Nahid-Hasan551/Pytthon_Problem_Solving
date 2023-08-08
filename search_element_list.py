mylist = [1, 6, 3, 5, 3, 4]
ele = int(input("Please Input number:"))
flag = 0
for i in mylist:
    if i == ele:
        print("Element Found")
        flag= 1
        break
if flag == 0:
    print("Element Not Found")
