number = int(input("Enter your number:"))
print("You entered number:", number)

count = 0
if number > 1:
    for i in range(1, number + 1):
        if (number % i) == 0:
            count = count + 1
    if count == 2:
      print("Your entred number is a prime number")
    else:
      print("your entered number is not a prime number")
